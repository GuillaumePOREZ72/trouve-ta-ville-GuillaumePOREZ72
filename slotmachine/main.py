import random

# Nombre maximum de lignes à miser
MAX_LINES = 3
# Montant maximum de mise
MAX_BET = 100
# Montant minimum de mise
MIN_BET = 1

# Nombre de lignes et de colonnes dans la machine à sous
ROWS = 3
COLS = 3

# Dictionnaire pour stocker le nombre de chaque symbole
symbol_count = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8
}

# Dictionnaire pour stocker la valeur de chaque symbole
symbol_value = {
  "A": 5,
  "B": 4,
  "C": 3,
  "D": 2
}


def check_winnings(columns, lines, bet, values):
  """
  Vérifie les gains dans la machine à sous.
  
  Args:
    columns (liste): Liste des colonnes dans la machine à sous
    lines (int): Nombre de lignes à miser
    bet (int): Montant de la mise
    values (dict): Dictionnaire des valeurs des symboles
    
  Returns:
    winnings (int): Gains totaux
    winning_lines (liste): Liste des lignes gagnantes
  """
  winnings = 0
  winning_lines = []
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol!= symbol_to_check:
        break
    else:
      winnings += values[symbol] * bet
      winning_lines.append(line + 1)
      
  return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
  """
  Génère une rotation aléatoire de la machine à sous.
  
  Args:
    rows (int): Nombre de lignes dans la machine à sous
    cols (int): Nombre de colonnes dans la machine à sous
    symbols (dict): Dictionnaire des symboles et de leur nombre
    
  Returns:
    columns (liste): Liste des colonnes dans la machine à sous
  """
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)
      
  columns = []
  for _ in range(cols):
    column = []
    current_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value)
      column.append(value)
  
    columns.append(column)
    
  return columns


def print_slot_machine(columns):
  """
  Affiche la rotation de la machine à sous.
  
  Args:
    columns (liste): Liste des colonnes dans la machine à sous
  """
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i!= len(columns) - 1:
        print(column[row], end=" | ")
      else:
        print(column[row], end="")
  
    print()


def deposit():
  """
  Dépose de l'argent dans la machine à sous.
  
  Returns:
    amount (int): Montant déposé
  """
  while True:
    amount = input("Combien voulez-vous déposer? $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Le montant doit être supérieur à 0.")
    else:
      print("Veuillez entrer un nombre valide.")
      
  return amount


def get_number_of_lines():
  # Boucle jusqu'à ce qu'un nombre de lignes valide soit entré
  while True:
    lines = input("Entrez le nombre de lignes à miser (1-" + str(MAX_LINES) + ")?")
    if lines.isdigit():
      lines = int(lines)
      # Vérifie si le nombre entré est dans la plage valide
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Entrez un nombre de lignes valide.")
    else:
      print("Veuillez entrer un nombre valide.")
      
  # Retourne le nombre de lignes valide
  return lines


def get_bet():
  # Boucle jusqu'à ce qu'un montant de mise valide soit entré
  while True:
    amount = input("Quel est le montant que vous souhaitez miser sur chaque ligne? $")
    if amount.isdigit():
      amount = int(amount)
      # Vérifie si le montant entré est dans la plage valide
      if MIN_BET <= amount <= MAX_BET:
        break
      else:
        print(f"Le montant doit être entre ${MIN_BET} - ${MAX_BET}.")
    else:
      print("Veuillez entrer un nombre valide.")

  # Retourne le montant de mise valide
  return amount


def spin(balance):
  # Obtient le nombre de lignes à miser
  lines = get_number_of_lines()
  while True:
    # Obtient le montant de mise pour chaque ligne
    bet = get_bet()
    total_bet = bet * lines
    
    # Vérifie si le montant total de mise est dans le solde
    if total_bet > balance:
      print(f"Vous n'avez pas assez pour miser ce montant, votre solde actuel est : ${balance}")
    else:
      break
    
  # Affiche les informations de mise
  print(f"Vous misez ${bet} sur {lines} lignes. Le montant total de mise est égal à : ${total_bet}")  
    
  # Fait tourner la machine à sous
  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)
  # Vérifie les gains
  winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
  print(f"Vous avez gagné {winnings}.")
  print(f"Vous avez gagné sur les lignes :", *winning_lines)
  # Retourne le solde mis à jour
  return winnings - total_bet


def main():
  # Initialise le solde
  balance = deposit()
  while True:
    # Affiche le solde actuel
    print(f"Solde actuel : ${balance}")
    answer = input("Appuyez sur Entrée pour jouer (q pour quitter).")
    if answer == "q":
      break
    # Met à jour le solde après chaque tour
    balance += spin(balance)
    
  # Affiche le solde final
  print(f"Vous avez fini avec ${balance}")  
  
  
# Démarre le jeu
main()