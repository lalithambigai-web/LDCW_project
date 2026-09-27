import textwrap
books = [
    {"title": "Die Hard: Year One", "author": "Howard Chaykin", "genre": "Action", "lang": "English", "rating": "4.2/5", "description": "A graphic novel prequel to the iconic movie, detailing John McClane's early days as a rookie beat cop in New York City during the bicentennial summer of 1976."},
    {"title": "The Terminal List", "author": "Jack Carr", "genre": "Action", "lang": "English", "rating": "4.7/5", "description": "A high stakes military thriller following Navy SEAL James Reece as he seeks revenge against a high level government conspiracy after his entire team is ambushed and killed."},
    {"title": "Without Remorse", "author": "Tom Clancy", "genre": "Action", "lang": "English", "rating": "4.6/5", "description": "An origin story set during Vietnam War featuring John Clark(formerly John Kelly), detailing to CIA operative as he embarks on a personal mission of vengeance."},
    {"title": "The Gray Man", "author": "Mark Greaney", "genre": "Action", "lang": "English", "rating": "4.5/5", "description": "The first novel in the Court Gentry series, following an elite freelance assassin and former CIA operative who becomes the target of an international manhunt across Europe."},
    {"title": "Ice Station", "author": "Matthew Reilly", "genre": "Action", "lang": "English", "rating": "4.4/5", "description": "A fast paced action novel where shane 'Scarecrow' Schofield and a squad of US Marines fight for survival at a remote Antarctic research station against rival foreign forces."},

    {"title": "Pahlawan Melayu", "author": "A. Rahman", "genre": "Action", "lang": "Bahasa", "rating": "4.6/5", "description": "A Malay action/ historical fiction novel centered on the courage, traditional martial skills, and honor of heroic warrir fighting for his people and land."},
    {"title": "Darah & Maruah", "author": "Ahmad Izham", "genre": "Action", "lang": "Bahasa", "rating": "4.5/5", "description": "This story revolves around high stakes conflict, personal loyaty, and defending family and community dignity against dangerous adversaries."},
    {"title": "Pendekar Kembara", "author": "Siti Nurhalim", "genre": "Action", "lang": "Bahasa", "rating": "4.3/5", "description": "Translated as the Wandering Warrior, it follows a skilled martial artist traveling through different lands, facing off against corrupt forceswhile defending the innocent."},
    {"title": "Sembilan Nyawa", "author": "Zulkifli Ahmad", "genre": "Action", "lang": "Bahasa", "rating": "4.7/5", "description": "This story follews an elusive protagonist who repeatedly survives lethal situations and deadly operational missions."},
    {"title": "Operasi Ribut", "author": "M. Nizam", "genre": "Action", "lang": "Bahasa", "rating": "4.4/5", "description": "A military or law enforcement acttion thriller detailing a tactical unit's high risk mission to neutralize a severe security threat."},

    {"title": "Veeran", "author": "M. Karunanidhi", "genre": "Action", "lang": "Tamil", "rating": "4.4/5", "description": "Meaning The Brave Warrior, this narrative showcases a heroic central character overcoming formidable opponents to protect his community."},
    {"title": "Por Kalidasa", "author": "S. Murugan", "genre": "Action", "lang": "Tamil", "rating": "4.5/5", "description":"Translated as War of Kalidasa, a action-packed story combining warrior drama and battle tactics in a struggle against tyrannical forces."},
    {"title": "Sura", "author": "K. Rajan", "genre": "Action", "lang": "Tamil", "rating": "4.2/5", "description": "Named Shark (a symbol of power and relentless grit), following a powerful protagonist who fights against organized crime or societal corruption."},
    {"title": "Kaban", "author": "T. Raman", "genre": "Action", "lang": "Tamil", "rating": "4.3/5", "description": "A high intensity action drama centered around a heroic figure tackling heavy adversity, crime, and high risk confrontations."},

    {"title": "Dragon Blade", "author": "Chen Long", "genre": "Action", "lang": "Mandarin", "rating": "4.5/5", "description": "A martial arts hero's tale centered around a legendary, power laden blade and high stakes battle between warring factions."},
    {"title": "Shadow Warrior", "author": "Zhang Wei", "genre": "Action", "lang": "Mandarin", "rating": "4.6/5", "description": "A story following a covert assassin operating from the shadows during a period of political turmoil and clan rivalries."},
    {"title": "Wuxia Legend", "author": "Jin Yong", "genre": "Action", "lang": "Mandarin", "rating": "4.9/5", "description": "A classic wuxia story showcasing martial arts masters, chivalry, internal energy (qi), and complex struggles within the jianghu (underworld/martial community)."},

    {"title": "The Silent Patient", "author": "Alex Michaelides", "genre": "Thriller", "lang": "English", "rating": "4.5/5", "description": "A psychological thriller about Alicia Berenson, a famous painter who suddenly shoots her husband five times and never speaks another word, and the criminal psychotherapist obsessed with uncovering her motive."},
    {"title": "Gone Girl", "author": "Gillian Flynn", "genre": "Thriller", "lang": "English", "rating": "4.8/5","description": "A mystery involving the sudden disappearance of Amy Dunne on her fifth wedding anniversary, leaving her husband Nick as the primary suspect amidst unraveling secrets and media frenzy."},
    {"title": "The Girl on the Train", "author": "Paula Hawkins", "genre": "Thriller", "lang": "English", "rating": "4.4/5", "description": "A psychological suspense novel following Rachel, a commuter who observes a seemingly perfect couple from her train window every day until she witnesses something shocking that entangles her in a missing person case."},
    {"title": "Behind Closed Doors", "author": "B.A. Paris", "genre": "Thriller", "lang": "English", "rating": "4.6/5", "description": "A thriller exploring the dark reality of a seemingly perfect marriage between Jack and Grace, where control, domestic entrapment, and survival take center stage."},
    {"title": "The Guest List", "author": "Lucy Foley", "genre": "Thriller", "lang": "English", "rating": "4.3/5", "description": "A locked room mystery set on a remote island off the coast of Ireland during a celebrity wedding, where old resentments surface and a murder occurs during the storm bound reception."},

    {"title": "Sumpah Pembunuh", "author": "Ramlee Awang Murshid", "genre": "Thriller", "lang": "Bahasa", "rating": "4.8/5", "description": "A suspenseful story following an assassin or vengeful figure bound by a dangerous oath that leads to psychological conflict and high intensity pursuit."},
    {"title": "Misteri Rumah Tua", "author": "A. Samad", "genre": "Thriller", "lang": "Bahasa", "rating": "4.3/5", "description":"An atmospheric thriller focusing on dark secrets, mysterious occurrences, and hidden historical truths uncovered inside an abandoned mansion."},
    {"title": "Bayangan Maut", "author": "Khadijah Hashim", "genre": "Thriller", "lang": "Bahasa", "rating": "4.5/5", "description":"A mystery novel revolving around suspenseful threats, stalkers, and characters trying to escape an impending murder plot."},
    {"title": "Jejak Rahsia", "author": "Faisal Tehrani", "genre": "Thriller", "lang": "Bahasa", "rating": "4.4/5", "description":"An investigative thriller where the protagonist uncovers hidden clues, state secrets, or criminal webs leading to dangerous confrontations."},
    {"title": "Jerat", "author": "Tunku Halim", "genre": "Thriller", "lang": "Bahasa", "rating": "4.6/5", "description":"A psychological horror/thriller exploring dark human nature, sinister traps, and urban legends."},

    {"title": "Kottai Purathu Veedu", "author": "Indra Soundar Rajan", "genre": "Thriller", "lang": "Tamil", "rating": "4.8/5", "description":"A supernatural suspense thriller about mysterious deaths and paranormal occurrences surrounding an ancient fort house, investigated through a lens of myth and rationality."},
    {"title": "Kolaiyuthir Kaalam", "author": "Sujatha", "genre": "Thriller", "lang": "Tamil", "rating": "4.7/5", "description":"A crime thriller featuring famous duo Ganesh and Vasanth as they investigate unexplained occurrences involving an heiress, blending high-tech concepts with mysterious events."},
    {"title": "Nylon Kayiru", "author": "Sujatha", "genre": "Thriller", "lang": "Tamil", "rating": "4.6/5", "description":"A fast paced detective mystery (Sujatha's debut novel) centered around an unsolved murder where a nylon cord was used as the weapon, solved through keen deduction."},
   
    {"title": "Midnight Hunt", "author": "Zhang Wei", "genre": "Thriller", "lang": "Mandarin", "rating": "4.6/5", "description":"A suspense thriller following a nocturnal pursuit, where a investigator or vigilante hunts down a serial criminal in the dark corners of the city."},
    {"title": "Bad Kids", "author": "Zijin Chen", "genre": "Thriller", "lang": "Mandarin", "rating": "4.8/5", "description":"A psychological suspense novel where three children accidentally film a murder taking place, leading to a dangerous game of blackmail and moral decay between the killer and the kids."},
    {"title": "The Long Night", "author": "Chen Zijin", "genre": "Thriller", "lang": "Mandarin", "rating": "4.7/5", "description":"A dark crime thriller where a group of dedicated individuals spend years sacrificing everything to uncover a deep political cover-up and systemic corruption."},
    {"title": "Silent Shadow", "author": "Li Ang", "genre": "Thriller", "lang": "Mandarin", "rating": "4.3/5", "description":"A thriller centered around an elusive killer or operative operating in the background, leaving very few clues for investigators to trace."},

    {"title": "Atomic Habits", "author": "James Clear", "genre": "Motivation", "lang": "English", "rating": "4.8/5", "description":"A practical framework for building good habits and breaking bad ones using small, incremental 1% improvements everyday."},
    {"title": "7 Habits of Highly Effective People", "author": "Stephen Covey", "genre": "Motivation", "lang": "English", "rating": "4.7/5", "description":"A classic self-improvement guide providing a principle centered approach to solving personal and professional problems."},
    {"title": "Mindset", "author": "Carol Dweck", "genre": "Motivation", "lang": "English", "rating": "4.6/5", "description":"A psychological study contrasting the 'fixed mindset' with the 'growth mindset,' showing how our beliefs about our abilities dictate our potential for success."},
    {"title": "Can't Hurt Me", "author": "David Goggins", "genre": "Motivation", "lang": "English", "rating": "4.9/5", "description":"An autobiography detailing Navy SEAL David Goggins' journey through extreme mental toughness, overcoming trauma, and pushing past physical limits using the '40% Rule.'"},
    {"title": "Deep Work", "author": "Cal Newport", "genre": "Motivation", "lang": "English", "rating": "4.5/5", "description":"A guide focused on the ability to concentrate without distraction on cognitively demanding tasks in an increasingly noisy and fragmented digital world."},

    {"title": "Ketenangan Jiwa", "author": "Ustaz Syed", "genre": "Motivation", "lang": "Bahasa", "rating": "4.7/5", "description":"A spiritual self-help book focused on achieving inner peace, mental calm, and emotional resilience through faith and mindful living.  "},
    {"title": "Bangkit Kembali", "author": "Dr. Tuah", "genre": "Motivation", "lang": "Bahasa", "rating": "4.6/5", "description":"A motivational guide on overcoming failure, rebuilding self confidence, and recovering from life's setbacks."},
    {"title": "Ubah Fikir Ubah Hidup", "author": "Ahmad Fadzli", "genre": "Motivation", "lang": "Bahasa", "rating": "4.5/5", "description":"A practical book exploring how reframing your mindset and thought patterns transforms daily life and long-term success."},
    {"title": "Langkah Kejayaan", "author": "Prof. Muhaya", "genre": "Motivation", "lang": "Bahasa", "rating": "4.8/5", "description":"Actionable advice and positive psychology strategies aimed at personal development, goal setting, and overall wellbeing."},
    {"title": "Kuasa Impian", "author": "Irfan Khairi", "genre": "Motivation", "lang": "Bahasa", "rating": "4.4/5", "description":"A guide focused on unleashing personal potential, setting ambitious life/financial goals, and turning aspirations into reality."},

    {"title": "Anbu & Vaazhkai", "author": "R. K. Narayan", "genre": "Motivation", "lang": "Tamil", "rating": "4.6/5", "description":"Reflections on human relationships, empathy, and personal harmony in everyday life."},
    {"title": "Enidhu Vaazhdhal", "author": "Suki Sivam", "genre": "Motivation", "lang": "Tamil", "rating": "4.8/5", "description":"Philosophical and practical insights on leading a fulfilling, balanced, and ethical life."},
    {"title": "Maname Nalam Dhaana", "author": "Dr. V. Maitreyan", "genre": "Motivation", "lang": "Tamil", "rating": "4.5/5","description":"A self help guide addressing mental health, stress management, and emotional stability."},
    {"title": "Vetri Namadhe", "author": "APJ Abdul Kalam", "genre": "Motivation", "lang": "Tamil", "rating": "4.9/5", "description":"Motivational writings encouraging youth and readers to dream big, work hard, and overcome obstacles."},
    {"title": "Nambikkai", "author": "Vairamuthu", "genre": "Motivation", "lang": "Tamil", "rating": "4.7/5", "description":"A reflective and inspiring work centered on hope, perseverance, and inner strength."},

    {"title": "Living with Intent", "author": "Master Lin", "genre": "Motivation", "lang": "Mandarin", "rating": "4.9/5", "description":"Mindfulness and self-realization principles focusing on living purposefully, managing energy, and daily mental clarity."},
    {"title": "Courage to be Disliked", "author": "Ichiro Kishimi", "genre": "Motivation", "lang": "Mandarin", "rating": "4.8/5","description":"Based on Adlerian psychology, this book explains how to free yourself from past traumas, external expectations, and the need for approval to achieve true happiness."},
    {"title": "Path to Success", "author": "Jack Ma", "genre": "Motivation", "lang": "Mandarin", "rating": "4.6/5", "description":"Insights into entrepreneurship, resilience through failure, leadership, and maintaining a forward-looking vision."},

    {"title": "It Ends with Us", "author": "Colleen Hoover", "genre": "Romance", "lang": "English", "rating": "4.7/5", "description":"An emotional romance novel following Lily Bloom as she navigates a painful past, a passionate yet complicated relationship with Ryle Kincaid, and the unexpected re-entry of her first love, Atlas Corrigan."},
    {"title": "The Love Hypothesis", "author": "Ali Hazelwood", "genre": "Romance", "lang": "English", "rating": "4.5/5","description":"A fake-dating STEM romance where Ph.D. candidate Olive Smith fake-dates a notoriously strict young professor, Dr. Adam Carlsen, leading to real feelings. "},
    {"title": "Beach Read", "author": "Emily Henry", "genre": "Romance", "lang": "English", "rating": "4.4/5", "description":"A literary romance about two rival authors with severe writer's block who spend the summer in neighboring beach houses and swap genres to challenge each other."},
    {"title": "Red, White & Royal Blue", "author": "Casey McQuiston", "genre": "Romance", "lang": "English", "rating": "4.6/5","description":"A romance following Alex Claremont-Diaz, the First Son of the United States, and Prince Henry of Wales, as their public rivalry turns into a secret love affair."},

    {"title": "Cinta Hijab", "author": "Anis Ayuni", "genre": "Romance", "lang": "Bahasa", "rating": "4.5/5","description":"A romance story centered around personal growth, faith, and romantic relationships as characters navigate tradition and modern love."},
    {"title": "Projek Memikat Suami", "author": "Ainis", "genre": "Romance", "lang": "Bahasa", "rating": "4.6/5", "description":"A lighthearted, romantic drama about a wife trying various creative strategies to win over and strengthen her marriage with her husband."},
    {"title": "Rindu Kamu", "author": "Siti Rosmizah", "genre": "Romance", "lang": "Bahasa", "rating": "4.8/5","description":"An intense, high drama Malay romance filled with misunderstandings, deep longing, emotional sacrifices, and reconciliation."},
    {"title": "Setia Hujung Nyawa", "author": "Fatin Nabila", "genre": "Romance", "lang": "Bahasa", "rating": "4.4/5", "description":"A romance novel centered around forced or arranged marriage that evolves into deep, enduring love against family hurdles."},
    {"title": "Dia Semanis Honey", "author": "Dhiya Zafira", "genre": "Romance", "lang": "Bahasa", "rating": "4.7/5", "description":"A sweet romantic comedy exploring playful banter, past connections, and the developing romance between two contrasting personalities."},

    {"title": "Vaanathil Oru Vennila", "author": "Ramanichandran", "genre": "Romance", "lang": "Tamil", "rating": "4.6/5","description":"A classic Tamil family-centered romance story dealing with interpersonal relationships, misunderstandings, and emotional devotion."},
    {"title": "Mercury Pookkal", "author": "Balakumaran", "genre": "Romance", "lang": "Tamil", "rating": "4.7/5","description":"A deeply character-driven romantic drama exploring urban relationships, emotional struggles, and human attachments."},
    {"title": "Pirivom Sandhippom", "author": "Sujatha", "genre": "Romance", "lang": "Tamil", "rating": "4.5/5","description":"A narrative exploring the twists of fate, temporary separations, and eventual reunions in modern relationships."},
    {"title": "Sila Nerangalil Sila Manidharagal", "author": "Jayakanthan", "genre": "Romance", "lang": "Tamil", "rating": "4.8/5","description":"Some People in Some Situations — a classic novel exploring societal hypocrisy, morality, and a young woman's struggle after an unexpected life-altering incident."},
    {"title": "Oru Kadhal Oru Kavithai", "author": "Sivasankari", "genre": "Romance", "lang": "Tamil", "rating": "4.4/5", "description":"A romantic drama delving into emotional attachment, personal choices, and the complexities of human relationships."},

    {"title": "First Love", "author": "Gu Long", "genre": "Romance", "lang": "Mandarin", "rating": "4.5/5", "description":"A novel touching upon early romance, youthful ideals, and emotional growth, written with Gu Long's signature poetic style."},

    {"title": "Dune", "author": "Frank Herbert", "genre": "Science Fiction", "lang": "English", "rating": "4.8/5","description":"A epic sci-fi masterpiece following Paul Atreides as his family takes control of the desert planet Arrakis, the sole source of the universe's most valuable substance, 'spice.'"},
    {"title": "Project Hail Mary", "author": "Andy Weir", "genre": "Science Fiction", "lang": "English", "rating": "4.9/5","descriptiom":"A lone astronaut wakes up with amnesia on a desperate space mission to discover a solution to save Earth from a star-dying extinction event."},
    {"title": "Ender's Game", "author": "Orson Scott Card", "genre": "Science Fiction", "lang": "English", "rating": "4.7/5", "description":"A classic science fiction novel about Ender Wiggin, a gifted young boy recruited into an elite military academy in space to prepare for an impending alien invasion."},
    {"title": "Neuromancer", "author": "William Gibson", "genre": "Science Fiction", "lang": "English", "rating": "4.4/5", "description":"The definitive cyberpunk novel following Case, a washed-up computer hacker hired for a dangerous ultimate hack against an artificial intelligence."},
    {"title": "Foundation", "author": "Isaac Asimov", "genre": "Science Fiction", "lang": "English", "rating": "4.6/5","description":"The start of an epic sci-fi series where mathematician Hari Seldon uses psychohistory to predict the fall of the Galactic Empire and creates a foundation to save humanity's knowledge."},

    {"title": "Dunia Keturunan", "author": "Adibah Amin", "genre": "Science Fiction","lang": "Bahasa", "rating": "4.3/5", "description":"A story examining societal structures, generational heritage, and the evolving tensions between traditional legacy and future progress."},

    {"title": "The Three-Body Problem", "author": "Liu Cixin", "genre": "Science Fiction", "lang": "Mandarin", "rating": "4.9/5", "description":" A hard science fiction novel detailing humanity's first contact with an alien civilization from the Alpha Centauri system preparing to invade Earth."},
    {"title": "The Wandering Earth", "author": "Liu Cixin", "genre": "Science Fiction", "lang": "Mandarin", "rating": "4.7/5", "description":"A speculative novella where humanity builds giant thrusters to propel Earth out of the Solar System to escape an impending solar explosion."},
    {"title": "Folding Beijing", "author": "Hao Jingfang", "genre": "Science Fiction", "lang": "Mandarin", "rating": "4.6/5", "description":"A Hugo Award-winning novelette set in a futuristic, physically folding Beijing where society is divided into three distinct social classes sharing a 48-hour cycle."},
    {"title": "Waste Tide", "author": "Chen Qiufan", "genre": "Science Fiction", "lang": "Mandarin", "rating": "4.4/5", "description":"A eco-tech thriller set on Silicon Isle, a near future electronic waste recycling hub where workers revolt against eco-disaster and corporate exploitation."},
    {"title": "Starry Sky", "author": "Wang Jinkang", "genre": "Science Fiction", "lang": "Mandarin", "rating":"4.5/5", "description":"A science fiction exploration of space exploration, cosmic morality, and the future evolution of human consciousness across the stars."}
]

def display_banner():
    banner = """
    ┌─────────────────────────────────────────────────────────────┐
    │  Welcome to Rakuten Kobo Ebooks                             │
    │                                                             │
    │            ██╗  ██╗  ██████╗  ██████╗   ██████╗             │
    │            ██║ ██╔╝ ██╔═══██╗ ██╔══██╗ ██╔═══██╗            │
    │            █████═╝  ██║   ██║ ██████╔╝ ██║   ██║            │
    │            ██╔═██╗  ██║   ██║ ██╔══██╗ ██║   ██║            │
    │            ██║  ██╗ ╚██████╔╝ ██████╔╝ ╚██████╔╝            │
    │            ╚═╝  ╚═╝  ╚═════╝  ╚═════╝   ╚═════╝             │
    │                                                             │
    └─────────────────────────────────────────────────────────────┘
    Kobo helps to discover and finds your e-books 
    ● Logged in as: Student
    """
    print(banner)
    

def main():
    genres = {
        "action": "Action", 
        "thriller": "Thriller", 
        "motivation": "Motivation", 
        "romance": "Romance", 
        "science fiction": "Science Fiction"
    }

    languages = {
        "english": "English",
        "tamil": "Tamil",
        "mandarin": "Mandarin",
        "bahasa": "Bahasa"
    }

    while True:
        display_banner()

        print("1. Book recomendation")
        print("2. View book details")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n")
            print("So, what genre are you looking for?")
            print("1. Action")
            print("2. Thriller")
            print("3. Motivation")
            print("4. Romance")
            print("5. Science Fiction")
            
            genre_choice = input("Select genre: ").strip().lower()
            while genre_choice not in genres:
                print("\n")
                print("---------------------------------------------------")
                print("Sorry, invalid genre! Please type the full genre name")
                print("---------------------------------------------------")
                print("\n")
                genre_choice = input("Select genre: ").strip().lower()
                
            selected_genre = genres[genre_choice]

            print("\n")
            print("In what language do you prefer?")
            print("1. English")
            print("2. Tamil")
            print("3. Mandarin")
            print("4. Bahasa")
            
            lang_choice = input("Select language: ").strip().lower()
            while lang_choice not in languages:
                print("\n")
                print("---------------------------------------------------")
                print("Sorry, invalid language! Please type the full language name")
                print("---------------------------------------------------")
                print("\n")
                lang_choice = input("Select language: ").strip().lower()
                
            selected_lang = languages[lang_choice]

            matching_books = []
            for book in books:
                if book["genre"] == selected_genre and book["lang"] == selected_lang:
                    matching_books.append(book)

            if matching_books:
                print("\n")
                print("-------------------------------------------------------------")
                print(f"Here are some {selected_genre.upper()} books in {selected_lang.upper()}:")
                print("-------------------------------------------------------------")
                print("\n")

                count = 1
                for book in matching_books:
                    print(f"{count}. Title  : {book['title']}")
                    print(f"   Author : {book['author']}")
                    print(f"   Rating : {book['rating']}")
                    print("-------------------------------------------------------------")
                    count += 1

                print("\n")
                print("---------------------------------------------------")
                ans = input("Okay, is this what you're looking for? (yes/no): ").strip().lower()
                while ans not in ["yes", "y", "no", "n"]:
                    print("\n")
                    print("---------------------------------------------------")
                    print("Sorry, invalid response! Please type 'yes' or 'no'")
                    print("---------------------------------------------------")
                    print("\n")
                    ans = input("Okay, is this what you're looking for? (yes/no): ").strip().lower()

                if ans in ["yes", "y"]:
                    print("\n")
                    print("---------------------------------------------------")
                    print("Thank youuu for choosing Kobo! Enjoy your reading")
                    print("---------------------------------------------------")
                    print("\n")
                    break

            else:
                print("\n")
                print("---------------------------------------------------")
                print("Oh nooo!! sorry no books found for this combination.")
                print("---------------------------------------------------")
                print("\n")
                retry_choice = input("Do you want to select genre again? (yes/no): ").strip().lower()
                while retry_choice not in ["yes", "y", "no", "n"]:
                    print("\n")
                    print("---------------------------------------------------")
                    print("Sorry, invalid response! Please type 'yes' or 'no'")
                    print("\n")
                    print("---------------------------------------------------")
                    retry_choice = input("Do you want to select genre again? (yes/no): ").strip().lower()

                if retry_choice in ["yes", "y"]:
                    continue
                else:
                    print("\n")
                    print("---------------------------------------------------")
                    print("Thank youuu for using Kobo! Goodbye!")
                    print("---------------------------------------------------")
                    break

        elif choice == "2":
            print("\n==================================")
            print("       List of Book Available       ")
            print("==================================\n")
            for index, book in enumerate(books, start=1):
                print(f"{index}. {book['title']}")

            book_choice = input("Enter the book number to view the details:")
            if book_choice.isdigit():
                selected_no = int(book_choice) - 1

                if 0 <= selected_no < len(books):
                    selected_book = books[selected_no]

                    
                    print("\n==================================================================")
                    print(f"Title       :{selected_book['title']}")
                    print(f"Author      :{selected_book['author']}")
                    print(f"Genre       :{selected_book['genre']}")
                    print(f"Rating      :{selected_book['rating']}")
                   
                    raw_description = selected_book['description'].strip()
                    prefix = "Description :"
                    wrapped_description = textwrap.fill(raw_description, width=60, initial_indent=prefix, subsequent_indent=" " * len(prefix))
                    print(wrapped_description)
                    print("==================================================================\n")
                    
                    input("\nPress Enter to return to the main menu...")
                else:
                    print("Invalid book number selection.")
                    input("\nPress Enter to return to the main menu...")

        elif choice == "3":
            print("Thank You for Choosing Kobo!!!")
            break

if __name__ == "__main__":
    main()