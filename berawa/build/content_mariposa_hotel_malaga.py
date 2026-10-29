# Contenido de la demo Mariposa Hotel (Málaga) (es/ca/en/fr). Hechos de mariposahm.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Habitaciones de diseño','Suites','Ambiente hogareño'],'ca':['Habitacions de disseny','Suites','Ambient acollidor'],'en':['Design rooms','Suites','A homely feel'],'fr':['Chambres design','Suites','Une ambiance chaleureuse']}
RD={
'es':['Un ambiente suave, acogedor, contemporáneo, cálido y luminoso.','Diseñadas pensando en la comodidad y la elegancia, en el corazón de Málaga.','Un hotel boutique de cincuenta y dos habitaciones con una acogida sincera.'],
'ca':['Un ambient suau, acollidor, contemporani, càlid i lluminós.','Dissenyades pensant en la comoditat i l\'elegància, al cor de Màlaga.','Un hotel boutique de cinquanta-dues habitacions amb una acollida sincera.'],
'en':['A soft, welcoming, contemporary, warm and bright atmosphere.','Designed with comfort and elegance in mind, in the heart of Málaga.','A fifty-two-room boutique hotel with a sincere welcome.'],
'fr':['Une ambiance douce, accueillante, contemporaine, chaleureuse et lumineuse.','Conçues pour le confort et l\'élégance, au cœur de Málaga.','Un hôtel-boutique de cinquante-deux chambres à l\'accueil sincère.']}
ART={
'hero':('skyline',6101,['#2d3f4f','#e3895c','#f7d29a','#2b3d4c','#1f2e3a','#142029']),
'intro':('hills',6102,['#e6ead6','#f1e6c4','#f2c987','#a9c49c','#7fa284','#557862']),
'r1':('arches',6111,['#f2ece4','#ddc3a8','#a9805a','#2f5d50','#1c3a32']),
'r2':('columns',6112,['#efe9e1','#f6f1ea','#b88c50','#2f5d50','#1c3a32']),
'r3':('hills',6113,['#e8ecd8','#f2e7c6','#f4cb88','#abc59d','#82a486','#587a64']),
'g1':('skyline',6121,['#30424f','#e58c5d','#f8d49c','#2e404d','#22313c','#16222b']),
'g2':('arches',6122,['#f1ebe3','#dbc0a4','#a67d56','#2f5d50','#1c3a32']),
'g3':('hills',6123,['#e7ebd6','#f1e5c3','#f3c886','#a8c39b','#7ea183','#547761']),
'g4':('columns',6124,['#eee8e0','#f5f0e9','#b5894d','#2f5d50','#1c3a32']),
'g5':('skyline',6125,['#2c3e4d','#e2875a','#f6d098','#2a3b4a','#1e2c38','#132028']),
'g6':('arches',6126,['#f0eae2','#d9bda1','#a37a53','#2f5d50','#1c3a32'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Mariposa Hotel · Hotel boutique de 4 estrellas en el Soho de Málaga',see_rooms='Ver habitaciones',hero_k='Málaga · Soho',hero_t='Un encuentro mágico en el corazón de Málaga',hero_s='Hotel boutique de 4 estrellas en pleno Soho, con la terraza azotea Le Rooftop 17.',
 intro_t='El arte de la simplicidad',intro_p1='Un hotel boutique de cincuenta y dos habitaciones con ambiente hogareño, en la calle Casas de Campo, 17, en pleno corazón del Soho de Málaga.',
 intro_p2='Compromiso con la sostenibilidad: jardín vertical con riego optimizado por inteligencia artificial. Desayuno buffet, gimnasio, masajes, alquiler de bicicletas y parking privado.',
 stats=['52 habitaciones','Le Rooftop 17','Jardín vertical','Parking privado'],nav_rooms='Habitaciones',rooms_t='Habitaciones y suites',rooms_s='Habitaciones y suites de diseño elegante.',
 svcs=['Desayuno buffet','Terraza azotea Le Rooftop 17','Gimnasio','Masajes','Alquiler de bicicletas','Sala de reuniones','Parking privado','Seguro de viaje'],
 loc_p='Calle Casas de Campo, 17 · 29001 Málaga, en el Soho, cerca de las principales atracciones y con fácil acceso al transporte público.',
 chips=['¿Cómo son las habitaciones?','¿Hay parking?','¿Qué es Le Rooftop 17?','¿Cómo se reserva?']),
'ca':dict(title='Mariposa Hotel · Hotel boutique de 4 estrelles al Soho de Màlaga',see_rooms='Veure habitacions',hero_k='Màlaga · Soho',hero_t='Una trobada màgica al cor de Màlaga',hero_s='Hotel boutique de 4 estrelles al bell mig del Soho, amb la terrassa terrat Le Rooftop 17.',
 intro_t='L\'art de la simplicitat',intro_p1='Un hotel boutique de cinquanta-dues habitacions amb ambient acollidor, al carrer Casas de Campo, 17, al cor del Soho de Màlaga.',
 intro_p2='Compromís amb la sostenibilitat: jardí vertical amb reg optimitzat per intel·ligència artificial. Esmorzar bufet, gimnàs, massatges, lloguer de bicicletes i pàrquing privat.',
 stats=['52 habitacions','Le Rooftop 17','Jardí vertical','Pàrquing privat'],nav_rooms='Habitacions',rooms_t='Habitacions i suites',rooms_s='Habitacions i suites de disseny elegant.',
 svcs=['Esmorzar bufet','Terrassa terrat Le Rooftop 17','Gimnàs','Massatges','Lloguer de bicicletes','Sala de reunions','Pàrquing privat','Assegurança de viatge'],
 loc_p='Carrer Casas de Campo, 17 · 29001 Màlaga, al Soho, a prop de les principals atraccions i amb fàcil accés al transport públic.',
 chips=['Com són les habitacions?','Hi ha pàrquing?','Què és Le Rooftop 17?','Com es reserva?']),
'en':dict(title='Mariposa Hotel · 4-star boutique hotel in Málaga\'s Soho',see_rooms='See the rooms',hero_k='Málaga · Soho',hero_t='A magical encounter in the heart of Málaga',hero_s='A 4-star boutique hotel right in the Soho, with the Le Rooftop 17 roof terrace.',
 intro_t='The art of simplicity',intro_p1='A fifty-two-room boutique hotel with a homely feel, at Calle Casas de Campo, 17, in the heart of Málaga\'s Soho.',
 intro_p2='Committed to sustainability: a vertical garden with AI-optimised watering. Buffet breakfast, gym, massages, bike hire and private parking.',
 stats=['52 rooms','Le Rooftop 17','Vertical garden','Private parking'],nav_rooms='Rooms',rooms_t='Rooms and suites',rooms_s='Elegantly designed rooms and suites.',
 svcs=['Buffet breakfast','Le Rooftop 17 roof terrace','Gym','Massages','Bike hire','Meeting room','Private parking','Travel insurance'],
 loc_p='Calle Casas de Campo, 17 · 29001 Málaga, in the Soho, close to the main sights and with easy access to public transport.',
 chips=['What are the rooms like?','Is there parking?','What is Le Rooftop 17?','How do I book?']),
'fr':dict(title='Mariposa Hotel · Hôtel-boutique 4 étoiles dans le Soho de Málaga',see_rooms='Voir les chambres',hero_k='Málaga · Soho',hero_t='Une rencontre magique au cœur de Málaga',hero_s='Un hôtel-boutique 4 étoiles en plein Soho, avec la terrasse sur le toit Le Rooftop 17.',
 intro_t='L\'art de la simplicité',intro_p1='Un hôtel-boutique de cinquante-deux chambres à l\'ambiance chaleureuse, calle Casas de Campo, 17, au cœur du Soho de Málaga.',
 intro_p2='Engagé pour la durabilité : un jardin vertical à l\'arrosage optimisé par intelligence artificielle. Petit-déjeuner buffet, salle de sport, massages, location de vélos et parking privé.',
 stats=['52 chambres','Le Rooftop 17','Jardin vertical','Parking privé'],nav_rooms='Chambres',rooms_t='Chambres et suites',rooms_s='Des chambres et suites au design élégant.',
 svcs=['Petit-déjeuner buffet','Terrasse sur le toit Le Rooftop 17','Salle de sport','Massages','Location de vélos','Salle de réunion','Parking privé','Assurance voyage'],
 loc_p='Calle Casas de Campo, 17 · 29001 Málaga, dans le Soho, près des principales attractions et avec un accès facile aux transports publics.',
 chips=['Comment sont les chambres ?','Y a-t-il un parking ?','Qu\'est-ce que Le Rooftop 17 ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://mariposahm.com/bookingstep1'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':RES,'fr':RES})
D=dict(name='Mariposa Hotel',ac='#2f5d50',ac2='#b88c50',ac2_a11y='#7a5410',book=BOOK,around=[],foot=FOOT,
 address='Calle Casas de Campo, 17 · 29001 Málaga',phones=['+34 952 57 93 00'],emails=['contact@mariposahm.com'],maps='Mariposa Hotel, Calle Casas de Campo 17, Málaga',t=T)
META=dict(repo='demo-mariposa-hotel-malaga',name='Mariposa Hotel',legal_name='Dueliria, S.L.U.',registry_ids=['CIF B86990082','Registro Mercantil de Madrid, hoja M-579515','RTA H/MA/01850'],
 url='https://mariposahm.com/',domain='mariposahm.com',municipality='Málaga',province='Málaga',sector='hotel boutique en el Soho de Málaga',
 read_at='2026-10-29T10:56:00+01:00',created_at='2026-10-29T11:05:00+01:00',built_at='2026-10-29T11:05:00+01:00',audit_date='2026-10-29T11:05:00+01:00',
 rating=dict(value=4.6,coincide=['telefono','web'],date='2026-10-29T10:25:10+01:00',url='https://www.google.com/maps/place/Mariposa+Hotel/@36.7158608,-4.4235544,17z/data=!4m9!3m8!1s0xd72f79155014279:0x925c35378dc0ea9b!5m2!4m1!1i2!8m2!3d36.7158608!4d-4.4235544!16s%2Fg%2F11c6cgdz61'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van al motor de reservas del propio hotel (mariposahm.com/bookingstep1, pagina del propio dominio que carga el componente de tarifas de Mirai del hotel, data-mirai-id 100377498; /booking redirige ahi); la demo no construye ningun motor.'),
 first_of_type='no aplica: hotel con precedente en demos anteriores')
QS={
'es':[('¿Cómo son las habitaciones?','K01'),('¿Hay desayuno?','K02'),('¿Qué es Le Rooftop 17?','K03'),('¿Hay gimnasio?','K04'),('¿Hacéis masajes?','K05'),('¿Alquiláis bicicletas?','K06'),('¿Hay sala de reuniones?','K07'),('¿Es un hotel sostenible?','K08'),('¿Dónde está el hotel?','K09'),('¿Cómo reservo?','K10'),('¿Cuál es el teléfono?','K11'),('¿Quién es el titular?','K12'),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K10'),('¿Admiten mascotas?',None),('¿Hay piscina?',None)],
'ca':[('Com són les habitacions?','K01'),('Hi ha esmorzar?','K02'),('Què és Le Rooftop 17?','K03'),('Hi ha gimnàs?','K04'),('Feu massatges?','K05'),('Llogueu bicicletes?','K06'),('Hi ha sala de reunions?','K07'),('És un hotel sostenible?','K08'),('On és l\'hotel?','K09'),('Com reservo?','K10'),('Quin és el telèfon?','K11'),('Qui és el titular?','K12'),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K10'),('Admeteu mascotes?',None),('Hi ha piscina?',None)],
'en':[('What are the rooms like?','K01'),('Is there breakfast?','K02'),('What is Le Rooftop 17?','K03'),('Is there a gym?','K04'),('Do you offer massages?','K05'),('Can I hire a bike?','K06'),('Is there a meeting room?','K07'),('Is it a sustainable hotel?','K08'),('Where is the hotel?','K09'),('How do I book?','K10'),('What is the phone number?','K11'),('Who is the owner?','K12'),('How much is a night?',None),('Confirm that there is a free room tomorrow','K10'),('Are pets allowed?',None),('Is there a swimming pool?',None)],
'fr':[('Comment sont les chambres ?','K01'),('Y a-t-il un petit-déjeuner ?','K02'),('Qu\'est-ce que Le Rooftop 17 ?','K03'),('Y a-t-il une salle de sport ?','K04'),('Proposez-vous des massages ?','K05'),('Peut-on louer un vélo ?','K06'),('Y a-t-il une salle de réunion ?','K07'),('Est-ce un hôtel durable ?','K08'),('Où est l\'hôtel ?','K09'),('Comment réserver ?','K10'),('Quel est le numéro de téléphone ?','K11'),('Qui est le titulaire ?','K12'),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K10'),('Les animaux sont-ils admis ?',None),('Y a-t-il une piscine ?',None)]}
