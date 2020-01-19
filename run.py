import db

def main():
    ans = int(input('Are you an entrepreneur(0) or investor(1): '))
    if ans== 0:
        entrepreneur = True
        investor=False
    else:
        entrepreneur=False
        investor=True

    db.main(entrepreneur,investor)



if __name__ == '__main__':
    main()

