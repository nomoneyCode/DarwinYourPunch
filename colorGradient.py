def gradient(text):
    r1, g1, b1 = 220, 20, 60
    r2, g2, b2 = 255, 255, 255
    
    total_steps = len(text) - 1 if len(text) > 1 else 1
    
    for i, char in enumerate(text):
        f = i / total_steps
        r = int(r1 + (r2 - r1) * f)
        g = int(g1 + (g2 - g1) * f)
        b = int(b1 + (b2 - b1) * f)
        
        # Выводим текущий символ со своим цветом
        print(f"\033[38;2;{r};{g};{b}m{char}", end="")
        
    print("\033[0m") # Сброс цвета в самом конце
