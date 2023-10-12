import backend

def main():
    company_details = {
        'name': input("Enter company name: "),
        # Prompt for other details as needed
    }

    use_cases = backend.generate_use_cases(company_details)
    print(use_cases)

if __name__ == "__main__":
    main()
