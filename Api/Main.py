def parse_status(data: dict[str, str]) -> str:
    match data.get("status"):
        case "active":
            return f"System {data.get('id')} is running smoothly."
        case _:
            return "Status unknown."

if __name__ == "__main__":
    test_data = {"status": "active", "id": "API_v2"}
    print(parse_status(test_data))
