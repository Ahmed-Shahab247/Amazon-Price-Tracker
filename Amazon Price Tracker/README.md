Amazon Price Tracker

A simple Python script that tracks the price of a product on Amazon and sends an email alert when the price drops below a specified threshold.

Features

✅ Web Scraping with BeautifulSoup – Extracts real-time price data from Amazon.

✅ Email Alerts – Sends an email when the price falls below your set limit.

✅ Cookie Handling – Uses cookies to bypass bot detection.

Setup Instructions

1. Install Dependencies

Make sure you have Python installed, then install the required libraries:

pip install requests
beautifulsoup4
python-dotenv


2. Configure Environment Variables

Create a .env file in the project directory and add your credentials:

EMAIL=your-email@gmail.com
PASSWORD=your-email-password
ADDRESS=recipient-email@gmail.com
USER_AGENT=your-browser-user-agent

3. Run the Script

Simply execute:

python main.py

Notes

The script relies on cookies from your browser to bypass Amazon's bot checks. You may need to update them periodically.

Ensure that Less Secure Apps is enabled for your email provider (or use an app password if using Gmail with 2FA).

Contributing

Feel free to fork this repository and submit pull requests for improvements! 🚀


