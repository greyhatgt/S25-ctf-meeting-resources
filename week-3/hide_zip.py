import sys
import subprocess

def convert_zip_to_c(zip_file, output_c="embed_zip.c", output_h="embedded_zip.h"):
    with open(zip_file, "rb") as f:
        zip_data = f.read()
    
    # Convert the ZIP data to a comma-separated list of hex values
    hex_data = ", ".join(f"0x{b:02x}" for b in zip_data)

    # Generate C header file that contains the ZIP data as a variable
    with open(output_h, "w") as f:
        f.write("#ifndef EMBEDDED_ZIP_H\n")
        f.write("#define EMBEDDED_ZIP_H\n\n")
        f.write(f"unsigned char embedded_zip[] = {{ {hex_data} }};\n")
        f.write(f"unsigned int embedded_zip_len = {len(zip_data)};\n\n")
        f.write("#endif // EMBEDDED_ZIP_H\n")

    print(f"[+] Generated {output_h} with embedded ZIP data.")

    # Generate C source file that includes the header
    c_code = '''#include <stdio.h>
#include "embedded_zip.h"

int main() {
    printf("I'm hiding something!\\n");
    printf("Try using 'binwalk --extract <this_binary>' to find out!\\n");
    return 0;
}
'''
    with open(output_c, "w") as f:
        f.write(c_code)

    print(f"[+] Generated {output_c} with a reference to the embedded ZIP data.")

def compile_c_program(output_c="embed_zip.c", output_binary="embed_zip"):
    compile_cmd = ["gcc", "-O0", output_c, "-o", output_binary]
    result = subprocess.run(compile_cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"[+] Successfully compiled {output_binary}.")
        print(f"    Run it using: ./{output_binary}")
        print(f"    Use binwalk to extract hidden ZIP: binwalk --extract {output_binary}")
    else:
        print(f"[-] Compilation failed: {result.stderr}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python embed_zip_tool.py <path_to_zip>")
        sys.exit(1)

    zip_input = sys.argv[1]
    convert_zip_to_c(zip_input)
    compile_c_program()
    