months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}
def data_conversion():
    while True:
        try:
            date = input("Date: ").title().strip()
            if "/" in date:
                date = date.split("/")
            else:
                date = date.replace(",", "").split(" ")
            year = date[2]
            month = date[0]
            day = int(date[1])
            if month.isdecimal():
                month = int(month)
                if month > 12:
                    continue
            if 0 <= day > 31:
                continue
            if month in months:
                print(f"{year}-{months[month]}-{day:02d}")
                break
            else:
                print(f"{year}-{month:02d}-{day:02d}")
                break

        except AttributeError:
            pass
        except IndexError:
            pass
        except EOFError:
            print()
            break
        except ValueError:
            pass

data_conversion()
