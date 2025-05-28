from agent.hsn_agent import HSNAgent

def run_agent():
    agent = HSNAgent()

    while True:
        print("\n🔎 Welcome to HSN Code Agent!")
        print("1. Validate HSN Code")
        print("2. Suggest HSN Code from Description")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            code = input("Enter HSN code to validate: ").strip()
            result = agent.validate_hsn_code(code)
            print("\n🧾 Result:")
            print(result['message'])
            if result['exists']:
                if result.get('hierarchy'):
                    print("🔗 Hierarchy:")
                    for parent_code, desc in result['hierarchy']:
                        print(f"  {parent_code} - {desc}")
        elif choice == '2':
            desc = input("Enter product description: ").strip()
            suggestions = agent.suggest_from_description(desc)
            print("\n💡 Suggestions:")
            for hsn, matched_desc, score in suggestions:
                print(f"  {hsn} - {matched_desc} (score: {score})")
        elif choice == '3':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    run_agent()
