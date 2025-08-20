import random
import fastapi

app = fastapi.FastAPI()

def generate_first_validate_number(nine_digits_cpf):
    counter = 10
    accumulator = 0
    for i in nine_digits_cpf:
        accumulator += int(i) * counter
        counter -= 1
    first_digit = accumulator * 10 % 11
    return str(first_digit) if first_digit <= 9 else '0'

def generate_second_validated_number(nine_digits_cpf):
    first_digit = generate_first_validate_number(nine_digits_cpf)
    nine_digits_cpf += first_digit
    counter = 11
    accumulator = 0
    for i in nine_digits_cpf:
        accumulator += int(i) * counter
        counter -= 1
    second_digit = accumulator * 10 % 11
    return str(second_digit) if second_digit <= 9 else '0'

def generate_cpf():
	cpf = ''
	for _ in range(9):
		cpf += str(random.randint(0, 9))
	return cpf

def validate_full_cpf(full_cpf):
    first_digit_validate = generate_first_validate_number(full_cpf[:9])
    second_digit_validate = generate_second_validated_number(full_cpf[:10])
    return full_cpf == (full_cpf[:9] + first_digit_validate + second_digit_validate)

def generate_full_valid_cpf():
    cpf = generate_cpf()
    return cpf + generate_first_validate_number(cpf) + generate_second_validated_number(cpf)

""" def bot():
    full_cpf = generate_full_valid_cpf()
    print("Here is the full CPF:", full_cpf)
    input_cpf = input("Please enter a CPF to validate: ")
    if validate_full_cpf(input_cpf):
        print("The CPF is valid.")
    else:
        print("The CPF is invalid.")

if __name__ == "__main__":
    bot() """
    
@app.get("/generate_cpf")
def generate_cpf_endpoint():
    return {"cpf": generate_full_valid_cpf()}

@app.get("/validate_cpf/{cpf}")
def validate_cpf_endpoint(cpf: str):
    is_valid = validate_full_cpf(cpf)
    return {"valid": is_valid}