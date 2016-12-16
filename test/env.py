import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
UNIT_TEST_DIR = os.path.join(ROOT_DIR, "unit")
ACCEPTANCE_TEST_DIR = os.path.join(ROOT_DIR, "acceptance")
RESOURCES_DIR = os.path.join(ROOT_DIR, "resources")
TEST_LIBS_DIR = os.path.join(RESOURCES_DIR, "testlibs")
RESULTS_DIR = os.path.join(ROOT_DIR, "results")
HTTP_SERVER_FILE = os.path.join(RESOURCES_DIR, "testserver", "testserver.py")
SRC_DIR = os.path.join(ROOT_DIR, "..", "src")

TRAVIS = os.environ.get("TRAVIS", False)
TRAVIS_EVENT_TYPE = os.environ.get("TRAVIS_EVENT_TYPE", [])
TRAVIS_JOB_NUMBER = os.environ.get("TRAVIS_JOB_NUMBER", "localtunnel")
SAUCE_USERNAME = os.environ.get("SAUCE_USERNAME", None)
SAUCE_ACCESS_KEY = os.environ.get("SAUCE_ACCESS_KEY", None)


sys.path.insert(0, SRC_DIR)
sys.path.append(UNIT_TEST_DIR)
