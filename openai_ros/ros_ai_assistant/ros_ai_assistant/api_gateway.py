#!/usr/bin/env python3
import threading

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from typing import Optional


app = Flask(__name__)
api = Api(app)


class APIGateway(Node):
    def __init__(self):
        super().__init__("api_gateway")

        self.cmd_pub = self.create_publisher(String, "ai_assistant/openai_request", 10)
        self.resp_sub = self.create_subscription(
            String, "ai_assistant/openai_response", self.on_response, 10
        )

        self.last_response = None

        t = threading.Thread(target=self._run_flask, daemon=True)
        t.start()

        self.get_logger().info("API Gateway node started")

    def _run_flask(self):
        # Flask в отдельном потоке
        app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)

    def publish_request(self, text: str):
        msg = String()
        msg.data = text
        self.cmd_pub.publish(msg)
        self.get_logger().info(f"Отправлен запрос в OpenAIIntegration: {text!r}")

    def on_response(self, msg: String):
        self.last_response = msg.data
        self.get_logger().info(f"Получен ответ от OpenAIIntegration: {msg.data!r}")


gateway_node: Optional[APIGateway] = None



class CommunicationEndpoint(Resource):
    def post(self, endpoint):
        global gateway_node
        if gateway_node is None:
            return {"error": "gateway_node not ready"}, 500

        data = request.get_json(force=True) or {}
        text = data.get("message", "")

        gateway_node.publish_request(text)

        # для простоты сразу возвращаем подтверждение
        return {
            "status": "queued",
            "endpoint": endpoint,
            "sent_text": text,
        }


api.add_resource(CommunicationEndpoint, "/api/v1/communication/<string:endpoint>")


def main(args=None):
    global gateway_node
    rclpy.init(args=args)
    gateway_node = APIGateway()
    try:
        rclpy.spin(gateway_node)
    finally:
        gateway_node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
