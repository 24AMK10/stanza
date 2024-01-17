import faker
import random

fake = faker.Faker()

data = {}

katraj_pincodes = [411037, 411043, 411046]
localities = ["dhankawadi", "katraj", "karvenagar"]
place_type = ["unisex", "male", "female"]
random_house = ["home", "house", 'apartment']

for _ in range(100):
    data['title'] = fake.catch_phrase()
    data['place'] = f"{fake.first_name()}'s {random_house[random.randint(0, 2)]}"
    data['mail'] = fake.email()
    data['state'] = 'Maharashtra'
    data['occupancy'] = random.randint(2, 5)
    data["image_url"] = fake.image_url()
    data["phone"] = fake.phone_number()
    data['pincode'] = katraj_pincodes[random.randint(0, 2)]
    data['locality'] = localities[random.randint(0, 2)]
    data["place_type"] = place_type[random.randint(0, 2)]
    data["rating"] = random.randint(2, 5)

    print(data)

