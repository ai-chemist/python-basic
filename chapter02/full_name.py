first_name = "arthur"
last_name = "morgan"

# f"{ }" 문자열 내에서 변수 사용
full_name = f"{first_name} {last_name}"

print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)