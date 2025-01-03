print("Page Replacement - FIFO Algorithm")

# Input total number of pages
pages = int(input("\nEnter Total Number of Pages: "))
Reference_string = []

# Input the reference string
print("\nEnter values of the Reference String:")
for m in range(pages):
    Reference_string.append(int(input(f"Value No.[{m + 1}]: ")))

# Input total number of frames
frames = int(input("\nEnter Total Number of Frames: "))
temp = [-1] * frames  # Initialize frames with -1 (empty)
page_faults = 0
current_index = 0  # To track which frame to replace

# Process the reference string
for m in range(pages):
    # Check if the page is already in the frame
    if Reference_string[m] not in temp:
        # Page fault occurs, replace the page using FIFO
        temp[current_index] = Reference_string[m]
        current_index = (current_index + 1) % frames  # Move to the next frame
        page_faults += 1

    # Print the current state of frames
    print("\nFrame Status after accessing page", Reference_string[m], ":")
    for n in range(frames):
        if temp[n] != -1:
            print(temp[n], end="\t")
        else:
            print("-", end="\t")

# Output total page faults
print("\n\nTotal Page Faults:", page_faults)
