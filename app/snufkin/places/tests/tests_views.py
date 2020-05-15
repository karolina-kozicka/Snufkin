import json
from django.test import TestCase
from django.urls import reverse

from snufkin.places.models import Place
from snufkin.users.factories import UserFactory
from snufkin.places.factories import PlaceFactory
from snufkin.users.views import LoginView


class PlacesListViewTests(TestCase):
    def test_redirects_to_login_if_user_is_not_authenticated(self):
        response = self.client.get(reverse("places:list"))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse("places:list"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.resolver_match.func.__name__, LoginView.as_view().__name__
        )

    def test_renders_list_template(self):
        user = UserFactory.create()
        self.client.force_login(user)
        response = self.client.get(reverse("places:list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], "places/list.html")

    def test_puts_places_to_context(self):
        user = UserFactory.create()
        places = PlaceFactory.create_batch(5, user=user)
        self.client.force_login(user)
        response = self.client.get(reverse("places:list"))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context.get("places"), places, transform=lambda x: x, ordered=False
        )


class PlacesDetailViewTests(TestCase):
    def test_redirects_to_login_if_user_is_not_authenticated(self):
        url = reverse("places:detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.resolver_match.func.__name__, LoginView.as_view().__name__
        )

    def test_renders_detail_template(self):
        user = UserFactory.create()
        place = PlaceFactory.create(user=user)
        self.client.force_login(user)
        url = reverse("places:detail", args=(place.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], "places/detail.html")

    def test_puts_place_to_context(self):
        user = UserFactory.create()
        place = PlaceFactory.create(user=user)
        self.client.force_login(user)
        url = reverse("places:detail", args=(place.id,))
        response = self.client.get(url)
        self.assertContains(response, place.name)


class PlacesDeleteViewTests(TestCase):
    def test_redirects_to_login_if_user_is_not_authenticated(self):
        url = reverse("places:delete", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.resolver_match.func.__name__, LoginView.as_view().__name__
        )

    def test_renders_delete_template(self):
        user = UserFactory.create()
        place = PlaceFactory.create(user=user)
        self.client.force_login(user)
        url = reverse("places:delete", args=(place.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], "places/delete.html")

    def test_puts_place_to_context(self):
        user = UserFactory.create()
        place = PlaceFactory.create(user=user)
        self.client.force_login(user)
        url = reverse("places:delete", args=(place.id,))
        response = self.client.get(url)
        self.assertContains(response, place.name)

    def test_deletes_place(self):
        user = UserFactory.create()
        place = PlaceFactory.create(user=user)
        self.client.force_login(user)
        url = reverse("places:delete", args=(place.id,))
        self.client.post(url)
        self.assertFalse(Place.objects.filter(id=place.id).exists())


class PlacesAddViewTests(TestCase):
    def test_redirects_to_login_if_user_is_not_authenticated(self):
        response = self.client.get(reverse("places:add"))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse("places:add"), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.resolver_match.func.__name__, LoginView.as_view().__name__
        )

    def test_renders_add_template(self):
        user = UserFactory.create()
        self.client.force_login(user)
        response = self.client.get(reverse("places:add"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], "places/add.html")

    def test_adds_place(self):
        user = UserFactory.create()
        self.client.force_login(user)
        response = self.client.post(
            reverse("places:add"),
            {
                "name": "Place",
                "point": json.dumps({"type": "Point", "coordinates": [20, 30]}),
            },
            follow=True,
        )
        self.assertEqual(response.template_name[0], "places/list.html")
        self.assertTrue(Place.objects.filter(name="Place", user=user).exists())


class PlacesEditViewTests(TestCase):
    def test_redirects_to_login_if_user_is_not_authenticated(self):
        url = reverse("places:edit", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.resolver_match.func.__name__, LoginView.as_view().__name__
        )

    def test_renders_edit_template(self):
        user = UserFactory.create()
        place = PlaceFactory.create(user=user)
        self.client.force_login(user)
        url = reverse("places:edit", args=(place.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], "places/edit.html")

    def test_edits_place(self):
        user = UserFactory.create()
        place = PlaceFactory.create(user=user)
        self.client.force_login(user)
        url = reverse("places:edit", args=(place.id,))
        response = self.client.post(
            url,
            {
                "name": "New_name",
                "point": json.dumps(
                    {"type": "Point", "coordinates": place.point.coords}
                ),
            },
            follow=True,
        )
        self.assertEqual(response.template_name[0], "places/list.html")
        self.assertTrue(
            Place.objects.filter(name="New_name", user=user, id=place.id).exists()
        )
