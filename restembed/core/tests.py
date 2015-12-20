from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone

def create_pred(s_l, s_w, p_l, pred, created_at):
  pred = IrisPrediction(sepal_length=s_l,
                        sepal_width=s_w,
                        petal_length=p_l,
                        prediction=pred,
                        created_at=timezone.now())
  return pred


class PredictionViewTests(TestCase):
  def test_index_with_manual_prediction(self):
    response=self.client.get(reverse('core:index'))

    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Iris")

