import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

def bar():
  try:
    raise EnvironmentError
  except EnvironmentError as e:
    logger.error("Failed to ")
    raise e


if __name__ == "__main__":
  bar()
