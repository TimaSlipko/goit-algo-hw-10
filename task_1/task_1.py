from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value


def main():
    model = LpProblem(name="prod", sense=LpMaximize)

    limonad = LpVariable(name="Лимонад", lowBound=0, cat='Integer')
    fruktovyi_sik = LpVariable(name="Фруктовий сік", lowBound=0, cat='Integer')

    model += limonad + fruktovyi_sik

    model += 2 * limonad + 1 * fruktovyi_sik <= 100
    model += 1 * limonad <= 50
    model += 1 * limonad <= 30
    model += 2 * fruktovyi_sik <= 40

    status = model.solve()

    print(f"Status: {LpStatus[status]}")
    print(f"Лимонад: {value(limonad)}")
    print(f"Фруктовий сік: {value(fruktovyi_sik)}")
    print(f"Total: {value(model.objective)}")

    water_used = 2 * value(limonad) + 1 * value(fruktovyi_sik)
    sugar_used = 1 * value(limonad)
    lemon_used = 1 * value(limonad)
    fruit_used = 2 * value(fruktovyi_sik)

    print(f"Вода: {water_used} / 100 (remainder: {100 - water_used})")
    print(f"Цукор: {sugar_used} / 50 (remainder: {50 - sugar_used})")
    print(f"Лимонний сік: {lemon_used} / (remainder: {30 - lemon_used})")
    print(f"Фруктове пюре: {fruit_used} / (remainder: {40 - fruit_used})")


if __name__ == "__main__":
    main()
