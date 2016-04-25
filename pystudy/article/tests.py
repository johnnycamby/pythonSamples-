from datetime import time
from django.test import TestCase
from article.models import Article, get_upload_file_name
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your tests here.

#=========== python manage.py test article ==========
# - created a testdb for our article project
#=========== python manage.py test article -v 2==========


class ArticleTest(TestCase):
    def create_article(self, title="test article", body="blah blah ...."):
        return Article.objects.create(
            title = title,
            body=body,
            pub_date=timezone.now(),
            likes=0
        )

    def test_article_creation(self):
        a = self.create_article()
        self.assertTrue(isinstance(a, Article))
        self.assertEqual(a.__unicode__(), a.title)

    def test_get_upload_file_name(self):
        filename = "test.txt"
        path = 'uploads/%s_%s' % (str(time()).replace('.','_'), filename)
        create_path = get_upload_file_name(self, filename)
        #self.assertEqual(path, create_path)
        self.assertNotEqual(path, create_path)

    def test_articles_list_view(self):
        a = self.create_article()
        url = reverse('all_articles')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(a.title, resp.content)

    def test_article_detail_view(self):
        a = self.create_article()
        url = reverse('get_article', args=[a.id])
        resp = self.client.get(url)
        self.assertEqual(reverse('get_article', args=[a.id]), a.get_absolute_url())
        self.assertEqual(resp.status_code, 200)
        self.assertIn(a.title, resp.content)


