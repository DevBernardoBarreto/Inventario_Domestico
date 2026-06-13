import os
from supabase import create_client


# Mantém os valores antigos como fallback para não quebrar o projeto.
# Em um projeto público, o ideal é usar variáveis de ambiente.
URL = os.getenv("SUPABASE_URL", "https://lafzhdadywcwxisujygm.supabase.co")
KEY = os.getenv("SUPABASE_KEY", "sb_publishable_6JPjxH1xN1S17jxT7Yuh8Q_VBbVkshp")

supabase = create_client(URL, KEY)
