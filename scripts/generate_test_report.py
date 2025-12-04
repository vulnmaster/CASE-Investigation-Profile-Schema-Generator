#!/usr/bin/env python3
"""
Test Report Generator for CASE Investigation Schema Generator.
Generates detailed test reports including coverage, test results, and validation status.
"""

import os
import sys
import json
import datetime
import subprocess
from pathlib import Path


def run_tests_with_coverage():
    """Run tests and return coverage data"""
    result = subprocess.run(
        [
            "pytest",
            "--cov=case_investigation_schema_generator",
            "tests/",
            "-v",
            "--json-report",
        ],
        capture_output=True,
        text=True,
    )
    return result.stdout, result.returncode


def generate_coverage_report():
    """Generate detailed coverage report"""
    subprocess.run(["coverage", "html"], capture_output=True)


def collect_test_results():
    """Collect and parse test results"""
    if not os.path.exists(".pytest_cache/v/cache/nodeids"):
        return None

    with open(".pytest_cache/v/cache/nodeids") as f:
        tests = f.readlines()

    return [test.strip() for test in tests]


def generate_report():
    """Generate comprehensive test report"""
    # Run tests and collect results
    test_output, exit_code = run_tests_with_coverage()
    test_results = collect_test_results()

    # Generate report data
    report = {
        "timestamp": datetime.datetime.now().isoformat(),
        "test_status": "PASSED" if exit_code == 0 else "FAILED",
        "total_tests": len(test_results) if test_results else 0,
        "test_output": test_output,
        "coverage_report": "coverage/index.html",
    }

    # Create reports directory if it doesn't exist
    Path("reports").mkdir(exist_ok=True)

    # Save report
    report_path = (
        f"reports/test_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)

    # Generate HTML coverage report
    generate_coverage_report()

    return report


def main():
    """Main function to generate test report"""
    try:
        report = generate_report()
        print(f"Test Report Generated:")
        print(f"Status: {report['test_status']}")
        print(f"Total Tests: {report['total_tests']}")
        print(f"Report saved to: reports/")
        print(f"Coverage report: {report['coverage_report']}")
        sys.exit(0 if report["test_status"] == "PASSED" else 1)
    except Exception as e:
        print(f"Error generating report: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
