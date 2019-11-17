import traceback

def run():
    try:
        int('hello')
    except Exception as e:
        print(traceback.format_exc(e))
        print(11)

if __name__ == "__main__":
    run()