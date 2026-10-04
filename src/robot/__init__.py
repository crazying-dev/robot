import robot.config as config
import robot.app as app
import signal
import sys

def handle_sigint(signum, frame):
	print("\n收到 Ctrl+C，准备退出...")
	sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)
print("程序运行中，按 Ctrl+C 退出")

def main() -> None:
	print("Hello from robot!")
	print(f"I will listen 0.0.0.0:{config.port}")
	print("="*20)
	app.run()
	
	