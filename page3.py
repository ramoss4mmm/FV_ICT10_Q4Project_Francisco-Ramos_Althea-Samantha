from pyscript import display,document

students = [

    {
        "name": "Ebtisam A Al Hazmi", 
        "photo": "images/ebitsam.png",
        "caption": "Glee Club"
    },
    {
        "name": "Yaniszsol Aeiou Alvarez",
        "photo": "images/yaniszolt.png",
        "caption": "MUN"
    },
    {
        "name": "Ethan Drei S Belsa",
        "photo": "images/ethan.png",
        "caption": "Volleyball"
    },
    {
        "name": "Giana Zoe Bernas", 
        "photo": "images/giana.png",
        "caption": "Science Club"
    },
    {
        "name": "Julianna Calaycay",
        "photo": "images/julianna.png",
        "caption": "Science Club"
    },
    {
        "name": "Jamie Alyanna Castelo", 
        "photo": "images/ashlei.png",
        "caption": "Intramurals"
    },
    {
        "name": "Francesca Meyer Cruz",
        "photo": "images/francesca.png",
        "caption": "Dance Club"
    },
    {
        "name": "Ely Defensor",
        "photo": "images/ely.png",
        "caption": "Christmas Party"
    },
    {
        "name": "Dannielle Luna Dimasuhid", 
        "photo": "images/dannielle.png",
        "caption": "Glee Club"
    },
    {
        "name": "Althea Mauri Francisco", 
        "photo": "images/althea.png",
        "caption": "JCO"
    },
    {
        "name": "Cristina Wen Hsu", 
        "photo": "images/ashlei.png",
        "caption": "Intramurals"
    },
    {
        "name": "Denise Juatchon", 
        "photo": "images/denise.png",
        "caption": "Friends"
    },
    {
        "name": "Judah Judge",
        "photo": "images/ashlei.png",
        "caption": "Intramurals"
    },
    {
        "name": "Francis Lilagan", 
        "photo": "images/francis.png",
        "caption": "Class Officer"
    },
    {
        "name": "Sam Luna",
        "photo": "images/sam.png",
        "caption": "Poetry and Public Speaking Festival"
    },
    {
        "name": "Enzo Josh Macaranas",
        "photo": "images/enzo.png",
        "caption": "Halloween Dance Performace"
    },
    {
        "name": "Pain Adler Mateo",
        "photo": "images/pain.png",
        "caption": "Marching Band"
    },
    {
        "name": "Ashley Mondragon",
        "photo": "images/ashley.png",
        "caption": "Marching Band"
    },
    {
        "name": "Lance Naldoza",
        "photo": "images/lance.png",
        "caption": "Math Club"
    },
    {
        "name": "Gabriel Emilio Natividad",
        "photo": "images/gab.png",
        "caption": "Class Officer"
    },
    {
        "name": "Sofia Ng",
        "photo": "images/sofia.png",
        "caption": "Science Club"
    },
    {
        "name": "Hendrich Mathis Ong",
        "photo": "images/hendrich.png",
        "caption": "JCO"
    },
    {
        "name": "Trisha Paz", 
        "photo": "images/trisha.png",
        "caption": "Top Scorer"
    },
    {
        "name": "Miguel Ramos", 
        "photo": "images/miguel.png",
        "caption": "Volunteer Work"
    },
    {
        "name": "Queeny Haraj Ramos", 
        "photo": "images/queeny.png",
        "caption": "Host"
    },
    {
        "name": "Samantha Ramos", 
        "photo": "images/samantha.png",
        "caption": "Gold Math Olympian"
    },
    {
        "name": "Ashlei Reodica", 
        "photo": "images/ashlei.png",
        "caption": "Intramurals"
    },
    {
        "name": "Vaughn Repolona", 
        "photo": "images/vaughn.png",
        "caption": "Photo Taking Competition"
    }

]

gallery = document.getElementById("gallery")

for student in students:

    gallery.innerHTML += f"""

    <div class='classbox'>

        <img src='{student["photo"]}'>

        <div class='name'>
            {student["name"]}
        </div>

        <div class='caption'>
            {student["caption"]}
        </div>

    </div>

    """