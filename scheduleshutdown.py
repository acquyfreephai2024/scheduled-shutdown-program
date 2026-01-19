import os
import platform
import datetime

def manual_shutdown_setup():
    print("--- Scheduled Shutdown Tool ---")
    
    try:
        # Get user input
        hour = int(input("Enter hour (0-23): "))
        minute = int(input("Enter minute (0-59): "))
        day_choice = input("Is this for today or tomorrow? (type 'today' or 'tomorrow'): ").strip().lower()
        
        day_offset = 1 if day_choice == "tomorrow" else 0
        
        # Calculate times
        now = datetime.datetime.now()
        target_date = now.date() + datetime.timedelta(days=day_offset)
        target_time = datetime.datetime.combine(target_date, datetime.time(hour, minute))
        
        # Calculate delay
        delay = (target_time - now).total_seconds()
        
        if delay < 0:
            print("\nError: The specified time has already passed for today.")
            return

        # OS Command Logic
        system = platform.system().lower()
        print(f"\nTarget confirmed: {target_time.strftime('%I:%M %p on %Y-%m-%d')}")
        
        if "windows" in system:
            os.system(f"shutdown /s /t {int(delay)}")
        else:
            # Linux/macOS uses minutes
            minutes = int(delay / 60)
            print("Note: You may be prompted for your computer password.")
            os.system(f"sudo shutdown -h +{minutes}")
            
        print("Shutdown scheduled successfully!")
        print("To cancel, use 'shutdown /a' (Windows) or 'sudo shutdown -c' (Mac/Linux).")

    except ValueError:
        print("Invalid input. Please enter numbers for time.")

if __name__ == "__main__":
    manual_shutdown_setup()