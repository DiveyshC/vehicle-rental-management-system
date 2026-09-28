from django.core.management.base import BaseCommand
from rental.models import Vehicle


class Command(BaseCommand):
    help = "Add sample vehicles to the database"

    def handle(self, *args, **kwargs):

        vehicles = [
            {
                "name": "Swift",
                "brand": "Maruti Suzuki",
                "model": "2025",
                "vehicle_type": "car",
                "registration_number": "MH01AA1001",
                "price_per_day": 1500,
                "seats": 5,
                "fuel_type": "petrol",
                "transmission": "manual",
                "description": "Reliable and economical hatchback suitable for city travel.",
            },
            {
                "name": "City",
                "brand": "Honda",
                "model": "2025",
                "vehicle_type": "car",
                "registration_number": "MH01AA1002",
                "price_per_day": 2200,
                "seats": 5,
                "fuel_type": "petrol",
                "transmission": "automatic",
                "description": "Comfortable sedan perfect for city and highway journeys.",
            },
            {
                "name": "Creta",
                "brand": "Hyundai",
                "model": "2025",
                "vehicle_type": "suv",
                "registration_number": "MH01AA1003",
                "price_per_day": 2500,
                "seats": 5,
                "fuel_type": "diesel",
                "transmission": "automatic",
                "description": "Premium SUV suitable for family trips and long-distance journeys.",
            },
            {
                "name": "Thar",
                "brand": "Mahindra",
                "model": "2025",
                "vehicle_type": "suv",
                "registration_number": "MH01AA1004",
                "price_per_day": 3000,
                "seats": 5,
                "fuel_type": "diesel",
                "transmission": "manual",
                "description": "Premium SUV suitable for city travel and adventure journeys.",
            },
            {
                "name": "Seltos",
                "brand": "Kia",
                "model": "2025",
                "vehicle_type": "suv",
                "registration_number": "MH01AA1005",
                "price_per_day": 2800,
                "seats": 5,
                "fuel_type": "petrol",
                "transmission": "automatic",
                "description": "Stylish SUV offering comfort, space and modern features.",
            },
            {
                "name": "Innova Crysta",
                "brand": "Toyota",
                "model": "2025",
                "vehicle_type": "suv",
                "registration_number": "MH01AA1006",
                "price_per_day": 3500,
                "seats": 7,
                "fuel_type": "diesel",
                "transmission": "automatic",
                "description": "Spacious seven-seater vehicle ideal for family and group travel.",
            },
            {
                "name": "Classic 350",
                "brand": "Royal Enfield",
                "model": "2025",
                "vehicle_type": "bike",
                "registration_number": "MH01AA1007",
                "price_per_day": 900,
                "seats": 2,
                "fuel_type": "petrol",
                "transmission": "manual",
                "description": "Classic motorcycle ideal for city rides and weekend trips.",
            },
            {
                "name": "MT-15",
                "brand": "Yamaha",
                "model": "2025",
                "vehicle_type": "bike",
                "registration_number": "MH01AA1008",
                "price_per_day": 850,
                "seats": 2,
                "fuel_type": "petrol",
                "transmission": "manual",
                "description": "Sporty and lightweight motorcycle for everyday riding.",
            },
            {
                "name": "Activa 6G",
                "brand": "Honda",
                "model": "2025",
                "vehicle_type": "bike",
                "registration_number": "MH01AA1009",
                "price_per_day": 600,
                "seats": 2,
                "fuel_type": "petrol",
                "transmission": "automatic",
                "description": "Comfortable scooter ideal for convenient city transportation.",
            },
            {
                "name": "3 Series",
                "brand": "BMW",
                "model": "2025",
                "vehicle_type": "luxury",
                "registration_number": "MH01AA1010",
                "price_per_day": 7500,
                "seats": 5,
                "fuel_type": "petrol",
                "transmission": "automatic",
                "description": "Luxury sedan offering a premium driving experience.",
            },
            {
                "name": "C-Class",
                "brand": "Mercedes-Benz",
                "model": "2025",
                "vehicle_type": "luxury",
                "registration_number": "MH01AA1011",
                "price_per_day": 8500,
                "seats": 5,
                "fuel_type": "petrol",
                "transmission": "automatic",
                "description": "Premium luxury sedan designed for comfort and elegance.",
            },
            {
                "name": "A4",
                "brand": "Audi",
                "model": "2025",
                "vehicle_type": "luxury",
                "registration_number": "MH01AA1012",
                "price_per_day": 8000,
                "seats": 5,
                "fuel_type": "petrol",
                "transmission": "automatic",
                "description": "Luxury sedan combining performance, comfort and modern design.",
            },
        ]

        added = 0
        skipped = 0

        for data in vehicles:

            vehicle, created = Vehicle.objects.get_or_create(
                registration_number=data["registration_number"],
                defaults=data,
            )

            if created:
                added += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Added: {vehicle.brand} {vehicle.name}"
                    )
                )
            else:
                skipped += 1
                self.stdout.write(
                    self.style.WARNING(
                        f"Already exists: {vehicle.brand} {vehicle.name}"
                    )
                )

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                f"Done! Added {added} vehicles, skipped {skipped} existing vehicles."
            )
        )