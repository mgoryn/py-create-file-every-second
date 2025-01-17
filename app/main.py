from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (
            f"app-{current_time.hour}_{current_time.minute}_"
            f"{current_time.second}.log"
        )
        file_content = str(current_time)

        with open(file_name, "w") as file:
            file.write(file_content)

        print(f"{file_content} {file_name}")

        sleep(1)
    pass


if __name__ == "__main__":
    main()
