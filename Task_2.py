import turtle

def draw_pythagorean_tree(branch_length, level):
    if level == 0:
        return
    
    # Малюємо основну гілку
    turtle.forward(branch_length)
    turtle.right(30)  # Поворот на 30 градусів
    
    # Рекурсивно малюємо праву гілку
    draw_pythagorean_tree(branch_length * 0.7, level - 1)
    
    turtle.left(60)  # Поворот на 60 градусів
    
    # Рекурсивно малюємо ліву гілку
    draw_pythagorean_tree(branch_length * 0.7, level - 1)
    
    turtle.right(30)  # Повертаємося назад на 30 градусів
    turtle.backward(branch_length)  # Повертаємося до попередньої позиції

def main():
    # Встановлюємо початкові параметри
    turtle.speed(0)  # Максимальна швидкість
    turtle.left(90)  # Орієнтуємо "черепаху" вгору
    turtle.up()
    turtle.backward(50)  # Відступаємо назад
    turtle.down()

    # Отримуємо рівень рекурсії від користувача
    level = int(input("Введіть рівень рекурсії: "))
    
    # Малюємо дерево
    draw_pythagorean_tree(50, level)  # Початкова довжина гілки

    turtle.done()

if __name__ == "__main__":
    main()