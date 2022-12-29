obem = int(input())
debit_parva_traba = int(input())
debit_vtora_traba = int(input())
missing_hours = float(input())
quantity_parva_traba = debit_parva_traba * missing_hours
quantity_vtora_traba = debit_vtora_traba * missing_hours
total_quantity_from_pipes = quantity_vtora_traba + quantity_parva_traba
fullness = total_quantity_from_pipes / obem * 100
first_pipe_contribution = quantity_parva_traba / total_quantity_from_pipes * 100
second_pipe_contribution = quantity_vtora_traba / total_quantity_from_pipes * 100
overflow = total_quantity_from_pipes - obem
if total_quantity_from_pipes <= obem:
    print(f"The pool is {fullness:.2f}% full. Pipe 1: {first_pipe_contribution:.2f}%. Pipe 2: {second_pipe_contribution:.2f}%.")
else:
    print(f"For {missing_hours:.2f} hours the pool overflows with {overflow:.2f} liters.")