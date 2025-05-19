import re

class DataSieve:
    
    #Cree un objet de la classe DataSieve, il garde le texte à analyser en mémoire
    #Il contient des méthodes pour extraire les emails, urls, numéros de téléphone, numéros de carte de crédit, heures, tags html, hashtags et devises
    def __init__(self, text):
        self.text = text 
    
    # cherche tout les emails dans le texte
    def extract_emails(self):
        return re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b',self.text)
    
    # cherche tout les urls dans le texte
    def extract_urls(self):
        return re.findall(r'https?://[a-zA-Z-0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?', self.text)
    
    # cherche tout les numéros de téléphone dans le texte
    # le format est (123) 456-7890 ou 123-456-7890 ou 123.456.7890
    def extract_phone_numbers(self):
        return re.findall(r'(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}',self.text)
    
    # cherche tout les numéros de carte de crédit dans le texte
    def extract_credit_cards(self):
        return re.findall(r'(?:\d{4}[-\s]?){3}\d{4}', self.text)
    
    # cherche tout les heures dans le texte
    # detecte l'heure dans le format 24h ou 12h(AM/PM)
    def extract_time(self):
        return re.findall(r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b', self.text)
    
    #cherche tout les tags html dans le texte
    def extract_html_tags(self):
        return re.findall(r'<[^>]+>', self.text)
    
    # cherche tout les hashtags dans le texte
    # un hashtag est un mot qui commence par #
    # et qui est suivi de lettres, chiffres ou _
    # le hashtag ne doit pas être suivi d'un espace ou d'un caractère spécial
    # le hashtag doit être au début ou après un espace
    # ou un caractère spécial
    def extract_hashtags(self):
        return re.findall(r'#\w+', self.text)
    
    # cherche tout les devises dans le texte
    # une devise est un mot qui commence par $
    # et qui est suivi de chiffres
    # le chiffre peut être suivi de , et de 2 chiffres
    def extract_currency(self):
        return re.findall(r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?', self.text)
    
    """Cette méthode appelle toutes les autres et retourne un dictionnaire contenant tous les résultats classés par type."""
    def extract_all(self):
        return {
            'emails': self.extract_emails(),
            'urls': self.extract_urls(),
            'phone_numbers': self.extract_phone_numbers(),
            'credit_cards': self.extract_credit_cards(),
            'time': self.extract_time(),
            'html_tags': self.extract_html_tags(),
            'hashtags': self.extract_hashtags(),
            'currency': self.extract_currency()
        }
    
if __name__ == "__main__":

        # Exemple d'utilisation
        text = """ Contact us at support@example.com or call (123) 456-7890. Visit https://www.example.com.
    Credit card: 1234-5678-9012-3456. Total: $1,234.56. Post at 2:30 PM <div class="main">#launch
    """
        parser = DataSieve(text)
        results = parser.extract_all() 

        for key, values in results.items():
            print(f"\n{key.capitalize()}:")
            for items in values:
                print(" -", items)
        """On crée un texte exemple (sample_text).

On crée un objet DataSieve avec ce texte.

On lance extract_all() pour tout récupérer.

On affiche les résultats type par type (emails, urls, etc.).

"""
