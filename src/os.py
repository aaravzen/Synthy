import layouts.controller as lc

layout_controller = lc.Controller()

def main():
    while True:
        layout_controller.sync()
        time.sleep(0.02)

if __name__ == "__main__": main()