Password Timing Attack Tool

This Python project demonstrates a timing attack on password validation systems, designed for educational purposes. The tool measures response times to infer the correct password by exploiting subtle timing discrepancies in login attempts.
Components

    Timing Attack Tool
    A Python script that uses aiohttp to asynchronously test password guesses. By measuring response times, it detects timing leaks to identify potential correct passwords.

    Mock Server
    A Flask-based server that simulates a vulnerable login system. It intentionally introduces timing delays to demonstrate how attackers can exploit timing vulnerabilities.

Requirements

    Python 3.x
    Flask (pip install flask)
    aiohttp (pip install aiohttp)

Usage
1. Run the Mock Server

python mock_server.py

This starts a local server at http://127.0.0.1:5000/login to simulate login attempts.
2. Run the Timing Attack Tool

python timing_attack.py

This tool will perform the timing attack on the mock server, logging response times and identifying potential matches based on timing discrepancies.
Key Features

    Asynchronous Requests: Efficient, concurrent password testing using aiohttp.
    Timing Leak Simulation: The mock server deliberately adds delays in validation to simulate vulnerable systems.
    Logging: Detailed logs for each password attempt, including response times and status.

Important

This tool is for educational purposes only. It should be used responsibly in authorized environments where you have explicit permission to test security.
