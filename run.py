import traceback

try:
    from yacut import app
except ImportError:
    traceback.print_exc()
    raise

if __name__ == '__main__':
    app.run()