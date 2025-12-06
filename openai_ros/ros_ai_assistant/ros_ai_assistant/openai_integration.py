#!/usr/bin/env python3
import os
import asyncio

import aiohttp
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class OpenAIIntegration(Node):
    def __init__(self):
        super().__init__("openai_integration")

        # параметры из launch или env
        self.declare_parameter("openai_api_key", "")
        self.declare_parameter("model", "gpt-4o-mini")

        self.api_key = self.get_parameter("openai_api_key").get_parameter_value().string_value
        if not self.api_key:
            self.api_key = os.environ.get("OPENAI_API_KEY", "")

        self.model = self.get_parameter("model").get_parameter_value().string_value or os.environ.get(
            "OPENAI_MODEL", "gpt-4o-mini"
        )

        if not self.api_key:
            self.get_logger().error("OPENAI_API_KEY не задан! Нода запустится, но отвечать не сможет.")

        # подписываемся на запросы и публикуем ответы
        self.subscription = self.create_subscription(
            String, "ai_assistant/openai_request", self.on_request, 10
        )
        self.publisher = self.create_publisher(String, "ai_assistant/openai_response", 10)

        self._loop = asyncio.new_event_loop()
        self._aio_task = asyncio.get_event_loop().run_in_executor(None, self._loop.run_forever)

        self.get_logger().info("OpenAIIntegration node started")

    def on_request(self, msg: String):
        text = msg.data
        self.get_logger().info(f"Получен запрос к OpenAI: {text!r}")

        async def _work():
            reply = await self.query_openai(text)
            out = String()
            out.data = reply
            self.publisher.publish(out)
            self.get_logger().info("Ответ OpenAI опубликован")

        asyncio.run_coroutine_threadsafe(_work(), self._loop)

    async def query_openai(self, prompt: str) -> str:
        if not self.api_key:
            return "[ОШИБКА] OPENAI_API_KEY не задан"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        body = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                "https://api.openai.com/v1/chat/completions", json=body, headers=headers
            ) as resp:
                data = await resp.json()
                try:
                    return data["choices"][0]["message"]["content"]
                except Exception:
                    return str(data)

def main(args=None):
    rclpy.init(args=args)
    node = OpenAIIntegration()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
