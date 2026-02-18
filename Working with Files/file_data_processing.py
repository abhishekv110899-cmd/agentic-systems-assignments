# file_data_processing.py

def read_numbers(filename):
    numbers = []
    
    # Open file using with statement
    with open(filename, "r") as file:
        print("File opened successfully")
        
        for line in file:
            clean_line = line.strip()   # remove whitespace
            if clean_line:              # avoid empty lines
                number = int(clean_line)
                numbers.append(number)
    
    return numbers


def compute_statistics(numbers):
    total_count = len(numbers)
    total_sum = sum(numbers)
    average = total_sum / total_count if total_count > 0 else 0
    
    return total_count, total_sum, average


def write_log(log_filename, count, total_sum, average):
    # Append mode
    with open(log_filename, "a") as log_file:
        log_file.write("File opened successfully\n")
        log_file.write(f"Read {count} numbers\n")
        log_file.write(f"Sum: {total_sum}\n")
        log_file.write(f"Average: {average}\n")
        log_file.write("Processing completed\n\n")


def main():
    input_file = "numbers.txt"
    log_file = "results.log"
    
    numbers = read_numbers(input_file)
    print("Data loaded successfully")
    
    count, total_sum, average = compute_statistics(numbers)
    print("Computation completed")
    
    write_log(log_file, count, total_sum, average)
    print("Results written to log file")


# Run program
main()