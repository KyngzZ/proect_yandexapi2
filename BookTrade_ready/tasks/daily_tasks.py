import schedule, time
def send_daily_email():
    print("Sending daily email...")

schedule.every().day.at("08:00").do(send_daily_email)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)