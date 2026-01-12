import sys
from TestWindow.test_application import TestApplication

def main():
    print("Hello from github-actions-test!")
    app = TestApplication()
    sys.exit(app.run())

if __name__ == "__main__":
    main()
