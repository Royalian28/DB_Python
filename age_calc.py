import pygame
import datetime

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 900, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Age Calculator')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)

# Fonts
font = pygame.font.Font(None, 25)
small_font = pygame.font.Font(None, 20)

# Background Color
BACKGROUND_COLOR = PINK

# Input box
input_rect = pygame.Rect(150, 200, 200, 32)
active = False
text = ''
placeholder_text = "dd-mm-yyyy"

# Calculate button
calculate = pygame.Rect(180, 250, 140, 50)

# Detailed age button
detailed = pygame.Rect(180, 320, 140, 50)

running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.size
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
                text = ''
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    try:
                        birth_date = datetime.datetime.strptime(text, '%d-%m-%Y')
                        today = datetime.datetime.now()
                        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                        age_text = f"{age}!!"
                    except ValueError:
                        age_text = "Invalid date format! Please use dd-mm-yyyy"

                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        # Button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if calculate.collidepoint(event.pos):
                try:
                    birth_date = datetime.datetime.strptime(text, '%d-%m-%Y')
                    today = datetime.datetime.now()
                    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                    age_text = f"{age}!!"
                except ValueError:
                    age_text = "Invalid date format! Please use dd-mm-yyyy"

            elif detailed.collidepoint(event.pos):
                try:
                    birth_date = datetime.datetime.strptime(text, '%d-%m-%Y')
                    today = datetime.datetime.now()
                    age = today - birth_date
                    years = age.days // 365
                    months = (age.days % 365) // 30
                    days = (age.days % 365) % 30
                    hours = age.seconds // 3600
                    minutes = (age.seconds % 3600) // 60

                    # Format the detailed age
                    age_detail_text = (
                        f"You have survived: {years} years\n"
                        f"{months} months, {days} days\n"
                        f"{hours} hours, {minutes} minutes"
                    )
                except ValueError:
                    age_detail_text = "Invalid date format! Please use dd-mm-yyyy"

    # Render input box
    pygame.draw.rect(screen, GRAY, input_rect, 2)
    input_surface = font.render(text if text else placeholder_text, True, BLACK)
    screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))

    # Render buttons
    pygame.draw.rect(screen, ORANGE, calculate)
    pygame.draw.rect(screen, ORANGE, detailed)

    calculate_text = font.render('Calculate Age', True, BLACK)
    detail_text = font.render('Detailed Age', True, BLACK)

    screen.blit(calculate_text, (185, 260))
    screen.blit(detail_text, (190, 330))

    # Display results
    try:
        result_surface = font.render(age_text, True, BLACK)
        screen.blit(result_surface, (150, 400))
    except NameError:
        pass

    try:
        # Render detailed age text line by line
        lines = age_detail_text.split('\n')
        for i, line in enumerate(lines):
            line_surface = font.render(line, True, WHITE)
            screen.blit(line_surface, (100, 400 + i * 30))
    except NameError:
        pass

    pygame.display.flip()

pygame.quit()
