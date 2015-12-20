from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import IrisPrediction

def create_pred(s_l, s_w, p_l, pred):
  pred = IrisPrediction.objects.create(sepal_length=s_l,
                        sepal_width=s_w,
                        petal_length=p_l,
                        prediction=pred,
                        created_at=timezone.now())
  return pred


class PredictionViewTests(TestCase):
  def test_index_with_no_prediction(self):
    response=self.client.get(reverse('core:index'))

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Iris")

  def test_index_shows_past_prediction(self):
    create_pred(1, 1, 1, 'Iris something')

    response=self.client.get(reverse('core:index'))
    self.assertContains(response, "something")


