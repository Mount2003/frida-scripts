import frida
import sys

def display_dict(data):
    print(data.keys())
    for key in data:
        if type(data[key]) == str or type(data[key]) == int:
            print(f'[i] Value of key "{key}" of type {type(data[key])}: "{data[key]}".')
        elif type(data[key]) == list:
            print(f'[i] Value of key "{key}" of type {type(data[key])}:')
            for item in data[key]:
                print(item)

def main():
    if len(sys.argv) < 2:
        print(f"Specify target exe to spawn: 'python {sys.argv[0]} target_app.exe'.")
        return 1
    elif len(sys.argv) > 2:
        print(f"Arguments more than 1, only one argument needed.")
        return 1
    
    pid = frida.spawn(sys.argv[1])
    print(f'Spawned process with PID: {pid}')
    
    try: 
        session = frida.attach(pid)
    except Exception as e:
        print(f'An error occured: {e}')
        
    with open('test.js', 'r') as f:
        js_code = f.read()
    script = session.create_script(f'''{js_code}''')

    def on_message(message, data):
        print(f'---------------------------------------------------------\nMessage: \n{message}\n')
        print(f'Data: \n{data}\n')
        if type(message) == dict:
            display_dict(message)

    script.on('message', on_message)
    script.load()

if __name__ == "__main__":
    main()
    
    