import os
import subprocess
import shlex

def execute_command(command):
    # Handle piping
    if "|" in command:
        commands = command.split("|")
        processes = []
        for i, cmd in enumerate(commands):
            cmd = shlex.split(cmd.strip())
            if i == 0:
                # First command
                processes.append(subprocess.Popen(cmd, stdout=subprocess.PIPE))
            elif i == len(commands) - 1:
                # Last command
                processes.append(subprocess.Popen(cmd, stdin=processes[-1].stdout))
            else:
                # Middle commands
                processes.append(subprocess.Popen(cmd, stdin=processes[-1].stdout, stdout=subprocess.PIPE))

        # Wait for the last process and fetch its output
        output, error = processes[-1].communicate()
        if output:
            print(output.decode())
        if error:
            print(error.decode())
        return

    # Handle input redirection
    if "<" in command:
        parts = command.split("<")
        cmd = shlex.split(parts[0].strip())
        input_file = parts[1].strip()
        with open(input_file, 'r') as infile:
            result = subprocess.run(cmd, stdin=infile, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(result.stdout.decode())
        return

    # Handle output redirection
    if ">" in command:
        parts = command.split(">")
        cmd = shlex.split(parts[0].strip())
        output_file = parts[1].strip()
        with open(output_file, 'w') as outfile:
            result = subprocess.run(cmd, stdout=outfile, stderr=subprocess.PIPE)
        return

    # Handle normal commands
    try:
        result = subprocess.run(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
        if result.stderr:
            print(result.stderr.decode())
    except FileNotFoundError:
        print(f"Command not found: {command}")

def main():
    print("Welcome to the Python Shell. Type 'exit' to quit.")
    while True:
        try:
            command = input("shell> ")
            if command.strip().lower() == "exit":
                break
            if command.strip():
                execute_command(command.strip())
        except KeyboardInterrupt:
            print("\nType 'exit' to quit.")
        except EOFError:
            break

if __name__ == "__main__":
    main()
