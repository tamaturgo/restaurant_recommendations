import pandas as pd
import requests
import random


# Lista de ruas
ruas = [
    'Rua Flores',
    'Rua das Árvores',
    'Rua do Sol',
    'Rua da Lua',
    'Rua do Mar',
    'Rua dos Ventos',
    'Rua do Campo',
    'Rua da Montanha',
    'Rua do Lago',
    'Rua da Fonte',
    'Rua dos Prazeres',
    'Rua do Paraíso',
    'Rua do Amor',
    'Rua do Sonho',
    'Rua do Tesouro',
    'Rua do Desejo',
    'Rua dos Anjos',
    'Rua das Estrelas',
    'Rua das Maravilhas',
    'Rua da Esperança'
]

# Lista de bairros
bairros = [
    'Centro',
    'Jardim',
    'Cidade Nova',
    'Liberdade',
    'Vila Nova',
    'São José',
    'Bom Jesus',
    'Santo Antônio',
    'São Francisco',
    'São Sebastião',
    'Santa Rita',
    'Vila Isabel',
    'Itapuã',
    'Barra',
    'Pelourinho',
    'Rio Vermelho',
    'Graça',
    'Pituba',
    'Itaigara',
    'Cabula'
]


# Lista de números
numeros = [str(i) for i in range(100)]

# Gerar 100 endereços aleatórios
enderecos = []
for i in range(100):
    rua = random.choice(ruas)
    bairro = random.choice(bairros)
    numero = random.choice(numeros)
    endereco = f'{rua}, {numero} - {bairro}'
    enderecos.append(endereco)

# Define uma lista de descrições para gerar descrições aleatórias

descricoes = [
    'O restaurante "La Brasserie" é um local sofisticado e elegante que serve pratos clássicos da cozinha francesa. Com um ambiente acolhedor e atendimento impecável, é uma excelente opção para uma noite especial.',
    'O "Steakhouse 21" é um paraíso para os amantes de carne, com uma seleção impressionante de cortes de alta qualidade. Com um ambiente moderno e descontraído, é perfeito para um jantar casual entre amigos.',
    'O "Sushimania" é um dos melhores restaurantes japoneses da cidade, com uma seleção variada de sushi, sashimi e outros pratos típicos da culinária japonesa. Com um ambiente contemporâneo e elegante, é uma opção perfeita para um jantar romântico.',
    'O "Bistro da Praça" é um restaurante charmoso que oferece pratos da cozinha internacional com um toque brasileiro. Com um ambiente aconchegante e um cardápio criativo, é uma excelente opção para um almoço de negócios.',
    'O "Cantinho do Mar" é um restaurante especializado em frutos do mar frescos, com um cardápio variado e uma atmosfera descontraída. Com vista para o mar, é um ótimo lugar para um jantar com amigos ou familiares.',
    'O "Bistrô da Vila" é um restaurante que oferece pratos da culinária italiana com um toque contemporâneo. Com um ambiente agradável e um cardápio criativo, é uma excelente opção para um jantar romântico.',
    'O "Boteco do Chico" é um bar e restaurante descontraído que serve pratos típicos da culinária brasileira, acompanhados de cerveja gelada e música ao vivo. Com um ambiente animado e descontraído, é uma ótima opção para um happy hour com amigos.',
    'O "Casa da Sopa" é um restaurante acolhedor que oferece uma variedade de sopas caseiras, acompanhadas de pães frescos e saladas. Com um ambiente confortável e um cardápio saudável, é uma excelente opção para um almoço leve.',
    'O "The Grill" é um restaurante sofisticado que oferece cortes de carne premium, preparados na grelha e acompanhados de molhos especiais. Com um ambiente elegante e um serviço impecável, é uma opção perfeita para um jantar especial.',
    'O "Cantina Italiana" é um restaurante que serve pratos da culinária italiana tradicional, preparados com ingredientes frescos e de alta qualidade. Com um ambiente acolhedor e um cardápio variado, é uma excelente opção para um jantar em família.',
    'O "Café do Museu" é um café charmoso que oferece uma seleção de cafés especiais, chás, bolos e outras delícias. Com um ambiente agradável e uma decoração vintage, é uma excelente opção para um café da tarde.',
    'O "Taj Mahal" é um restaurante que oferece pratos típicos da culinária indiana, preparados com temperos e especiarias exóticas.Com um ambiente elegante e uma decoração que remete à Índia, é uma excelente opção para uma experiência gastronômica diferente.',
    'O "Churrascaria do Sul" é um restaurante especializado em churrasco gaúcho, com uma seleção variada de cortes de carne e um rodízio com mais de 20 opções de pratos quentes e frios. Com um ambiente amplo e descontraído, é uma opção perfeita para um jantar com amigos ou familiares.',
    'O "Casa da Pizza" é um restaurante que oferece uma seleção variada de pizzas, acompanhadas de saladas e outros pratos italianos. Com um ambiente descontraído e um cardápio criativo, é uma excelente opção para um almoço casual entre amigos.',
    'O "Casa da Massa" é um restaurante que oferece uma seleção variada de massas frescas, acompanhadas de molhos especiais e outros pratos italianos. Com um ambiente descontraído e um cardápio criativo, é uma excelente opção para um almoço casual entre amigos.',
    'O "Casa da Carne" é um restaurante especializado em carnes, com uma seleção variada de cortes de alta qualidade, preparados na grelha. Com um ambiente descontraído e um cardápio criativo, é uma excelente opção para um almoço casual entre amigos.',
    'O "Thai House" é um restaurante que serve pratos típicos da culinária tailandesa, preparados com ingredientes frescos e temperos exóticos. Com um ambiente acolhedor e uma decoração que remete à Tailândia, é uma excelente opção para uma experiência gastronômica diferente.',
    'O "La Piazza" é um restaurante que oferece pratos da culinária italiana, como massas frescas, pizzas e risotos, em um ambiente descontraído e acolhedor. Com um cardápio variado e uma seleção de vinhos de qualidade, é uma excelente opção para um jantar em família.',
    'O "Brasileirinho" é um restaurante que serve pratos típicos da culinária brasileira, como feijoada, churrasco e moqueca, em um ambiente descontraído e alegre. Com música ao vivo nos finais de semana, é uma ótima opção para um happy hour com amigos.',
    'O "Sabor Peruano" é um restaurante que oferece pratos típicos da culinária peruana, como ceviche, lomo saltado e ají de gallina, em um ambiente acolhedor e autêntico. Com um cardápio criativo e uma decoração que remete ao Peru, é uma excelente opção para uma experiência gastronômica diferente.',
    'O "Jardim do Éden" é um restaurante vegetariano que oferece pratos saudáveis e saborosos, preparados com ingredientes frescos e orgânicos. Com um ambiente tranquilo e uma decoração rústica, é uma excelente opção para um almoço leve.',
    'O "Fratelli" é um restaurante que serve pratos da culinária italiana em um ambiente sofisticado e elegante. Com um cardápio criativo e uma seleção de vinhos de qualidade, é uma opção perfeita para um jantar romântico.',
    'O "Gaucho\'s" é um restaurante que oferece churrasco gaúcho em um ambiente amplo e descontraído, com música ao vivo nos finais de semana. Com uma seleção variada de cortes de carne e um rodízio de pratos quentes e frios, é uma ótima opção para um jantar com amigos ou familiares.',
    'O "Soul Kitchen" é um restaurante que oferece pratos saudáveis e saborosos, preparados com ingredientes orgânicos e de alta qualidade. Com um ambiente descontraído e uma decoração que remete à natureza, é uma excelente opção para um almoço leve.',
    'O "Sushiloko" é um restaurante que oferece pratos típicos da culinária japonesa, como sushis, sashimis e temakis, em um ambiente moderno e descontraído. Com um rodízio com mais de 30 opções de pratos, é uma ótima opção para um jantar com amigos.',
    'O "Churrascaria Brasa Viva" é um restaurante que oferece churrasco gaúcho em um ambiente rústico e aconchegante. Com uma seleção variada de cortes de carne e um rodízio com mais de 20 opções de pratos quentes e frios, é uma excelente opção para um jantar em família.',
    'O "Kebab House" é um restaurante que serve pratos típicos da culinária árabe, como kebab, falafel e homus, em um ambiente descontraído e acolhedor. Com um cardápio criativo e uma decoração que remete ao Oriente Médio, é uma ótima opção para um jantar com amigos.',
    'O "Graça da Vila" é um restaurante que serve pratos da culinária portuguesa, como bacalhau, caldo verde e arroz de pato, em um ambiente rústico e aconchegante. Com um cardápio variado e uma seleção de vinhos de qualidade, é uma excelente opção para um jantar em família.',
    'O "Taco Loco" é um restaurante que oferece pratos típicos da culinária mexicana, como tacos, burritos e guacamole, em um ambiente descontraído e animado. Com uma seleção de drinks criativos e uma decoração colorida, é uma ótima opção para um happy hour com amigos.',
    'O "Casa de Samba" é um restaurante que serve pratos típicos da culinária brasileira em um ambiente animado e descontraído, com música ao vivo de samba e pagode. Com uma seleção de drinks e petiscos, é uma excelente opção para uma noite de diversão com amigos.',
    'O "Marisqueira do Pedro" é um restaurante que serve pratos de frutos do mar frescos em um ambiente descontraído e acolhedor. Com uma seleção de vinhos e cervejas, é uma ótima opção para um jantar romântico ou uma refeição em família.',
    'O "Bistrô do Chef" é um restaurante que oferece pratos sofisticados e criativos em um ambiente elegante e refinado. Com uma seleção de vinhos de qualidade e uma decoração moderna, é uma excelente opção para um jantar especial ou uma celebração.',
    'O "Cantinho da Amizade" é um restaurante que serve pratos típicos da culinária portuguesa, como a açorda de camarão e o frango à cafreal, em um ambiente rústico e acolhedor. Com uma seleção de vinhos portugueses e uma decoração que remete às aldeias do país, é uma excelente opção para um jantar em família.',
    'O "Diner Americano" é um restaurante que oferece pratos típicos da culinária americana, como hambúrgueres e hot dogs, em um ambiente descontraído e nostálgico. Com uma seleção de milkshakes e sobremesas típicas, é uma ótima opção para um almoço com amigos ou uma refeição em família.',
    'O "La Dolce Vita" é um restaurante que serve pratos típicos da culinária italiana, como risotos e massas frescas, em um ambiente elegante e sofisticado. Com uma seleção de vinhos italianos e uma decoração inspirada na Toscana, é uma excelente opção para um jantar especial ou uma celebração.',
    'O "La Parrilla" é um restaurante que oferece churrasco argentino em um ambiente descontraído e acolhedor. Com uma seleção de cortes nobres de carne e um rodízio com mais de 20 opções de pratos quentes e frios, é uma ótima opção para um jantar com amigos ou uma refeição em família.',
    'O "Le Bistrô" é um restaurante francês que serve pratos sofisticados e criativos em um ambiente elegante e refinado. Com uma seleção de vinhos franceses e uma decoração inspirada em Paris, é uma excelente opção para um jantar especial ou uma celebração.',
    'O "Casa do Lombo" é um restaurante que serve pratos típicos da culinária portuguesa, como o famoso lombo de porco assado, em um ambiente rústico e acolhedor. Com uma seleção de vinhos portugueses e uma decoração que remete às casas de campo do país, é uma ótima opção para um jantar em família.',
    'O "Taste of India" é um restaurante que serve pratos típicos da culinária indiana, como o curry de cordeiro e o biryani, em um ambiente descontraído e aconchegante. Com uma seleção de chás indianos e uma decoração que remete às cores e texturas da Índia, é uma ótima opção para um jantar com amigos.',
    'O "Sabor de México" é um restaurante que oferece pratos típicos da culinária mexicana, como tacos e burritos, em um ambiente descontraído e colorido. Com uma seleção de tequilas e uma decoração que remete às festas mexicanas, é uma ótima opção para um jantar animado com amigos.',
    'O "Oriental Palace" é um restaurante que serve pratos típicos da culinária asiática, como o padang e o pho, em um ambiente moderno e sofisticado. Com uma seleção de vinhos asiáticos e uma decoração que remete aos palácios orientais, é uma excelente opção para um jantar especial ou uma celebração.',
    'O "La Cucina" é um restaurante italiano que serve pratos típicos da culinária do sul da Itália, como o gnocchi alla sorrentina e a parmigiana, em um ambiente aconchegante e informal. Com uma seleção de vinhos italianos e uma decoração que remete às casas de campo da região, é uma ótima opção para um jantar descontraído com amigos.',
    'O "Bar do Peixe" é um restaurante que serve pratos típicos da culinária litorânea, como moquecas e peixadas, em um ambiente descontraído e informal. Com uma seleção de cervejas artesanais e uma decoração que remete à praia, é uma ótima opção para um almoço em família ou uma refeição com amigos.',
    'O "Hummus House" é um restaurante que oferece pratos típicos da culinária árabe, como o hummus e o falafel, em um ambiente aconchegante e descontraído. Com uma seleção de chás árabes e uma decoração que remete às casas de chá do Oriente Médio, é uma ótima opção para um jantar com amigos.',
    'O "Brasa Churrascaria" é um restaurante que oferece churrasco brasileiro em um ambiente descontraído e acolhedor. Com uma seleção de cortes nobres de carne e um buffet com mais de 20 opções de acompanhamentos, é uma ótima opção para um almoço ou jantar em família.',
    'O "Green Kitchen" é um restaurante que serve pratos vegetarianos e veganos em um ambiente moderno e descontraído. Com uma seleção de sucos e smoothies naturais e uma decoração que remete à natureza, é uma ótima opção para quem busca opções saudáveis e sustentáveis.',
]


# Cria um DataFrame vazio para armazenar os dados dos restaurantes
restaurantes_df = pd.DataFrame(
    columns=['Nome', 'Endereço', 'Descrição', 'Imagem', 'Latitude', 'Longitude'])

index = 1
for desc in descricoes:
    # Pega o nome entre aspas
    nome = desc.split('"')[1]
    print(f"\n {index} - Gerando dados do restaurante: {nome}...")

    # Seleciona um endereço aleatório da lista de endereços
    endereco = random.choice(enderecos)

    # Seleciona uma descrição aleatória da lista de descrições
    descricao = desc

    # Faz uma requisição para uma API de imagens aleatórias de comida
    response = requests.get('https://source.unsplash.com/400x400/?food')

    # Define o caminho para salvar a imagem no disco
    caminho_imagem = f'static/img/restaurante_{index}.jpg'

    # Salva a imagem no disco
    with open(caminho_imagem, 'wb') as f:
        f.write(response.content)

    # Latitudes e longitudes aleatórias proximas a latitude e longitude (Latitude: -3.0968371 Longitude: -60.0365047)
    latitude = random.uniform(-3.0968371 - 0.04, -3.0968371 + 0.04)
    longitude = random.uniform(-60.0365047 - 0.04, -60.0365047 + 0.04)

    # Imprime os dados do restaurante
    print(f'Nome: {nome}')
    print(f'Endereço: {endereco}')
    print(f'Descrição: {descricao}')
    print(f'Caminho da imagem: {caminho_imagem}')
    print(f'Latitude: {latitude}')
    print(f'Longitude: {longitude}')

    # Adiciona os dados do restaurante no DataFrame
    restaurantes_df = restaurantes_df.append(
        {'Nome': nome, 'Endereço': endereco, 'Descrição': descricao, 'Imagem': caminho_imagem, 'Latitude': latitude, 'Longitude': longitude}, ignore_index=True)

    index += 1

restaurantes_df

# Salva os dados dos restaurantes em um arquivo CSV
restaurantes_df.to_csv('restaurantes.csv', index=False)
