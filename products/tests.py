from django.test import TestCase, override_settings

from .models import Category, Product, SiteSettings


@override_settings(ALLOWED_HOSTS=["lishu-floral-creations.onrender.com"])
class SearchDiscoveryTests(TestCase):
    def test_sitemap_and_canonical_use_request_host(self):
        host = "lishu-floral-creations.onrender.com"
        sitemap = self.client.get("/sitemap.xml", secure=True, HTTP_HOST=host)
        robots = self.client.get("/robots.txt", secure=True, HTTP_HOST=host)
        home = self.client.get("/", secure=True, HTTP_HOST=host)

        self.assertEqual(sitemap.status_code, 200)
        self.assertIn(f"https://{host}/", sitemap.content.decode())
        self.assertNotIn("example.com", sitemap.content.decode())
        self.assertNotIn("#product-", sitemap.content.decode())
        self.assertIn(
            f"Sitemap: https://{host}/sitemap.xml",
            robots.content.decode(),
        )
        self.assertContains(
            home,
            f'<link rel="canonical" href="https://{host}/">',
            html=True,
        )

    def test_contact_area_shows_address_and_google_maps_link(self):
        address = (
            "Ashwini Mallareddy Nadar, No 6, Siti, 3rd Floor, 5th main, "
            "2nd cross, Gare chinappa road, Mariyanna Palya, Hebbal "
            "Kempapura, Bengaluru, Karnataka 560024"
        )
        SiteSettings.objects.create(
            email="lishufloralcreations@gmail.com",
            address=address,
        )

        response = self.client.get(
            "/",
            HTTP_HOST="lishu-floral-creations.onrender.com",
        )

        self.assertContains(response, "lishufloralcreations@gmail.com")
        self.assertContains(response, address)
        self.assertContains(
            response,
            "https://www.google.com/maps/search/?api=1&amp;query=139%2C%20Guru%20Chinnappa%20Rd",
        )

    def test_custom_floral_keepsake_uses_custom_pricing_label(self):
        category = Category.objects.create(name="Custom Arrangements")
        Product.objects.create(
            name="Custom Floral Keepsake",
            description="A personalized handmade floral gift.",
            price="1799.00",
            image="products/custom-floral-keepsake.jpg",
            category=category,
        )

        response = self.client.get(
            "/",
            HTTP_HOST="lishu-floral-creations.onrender.com",
        )

        self.assertContains(response, "Price varies by customization")
        self.assertNotContains(response, "₹1799")
