from django.db import models

from accounting.models import Account


class ProblemSet(models.Model):
    title = models.CharField(max_length=100, blank=True, default='Untitled')
    author = models.ForeignKey(Account, on_delete=models.DO_NOTHING, default=None, null=True)

    def __str__(self):
        return self.title

    def get_top_accounts(self):
        from solutionManager.models import Solution
        solutions = Solution.objects.filter(problem__problem_set=self)
        top_account_by_accountId = dict()
        for solution in solutions:
            if not top_account_by_accountId.__contains__(solution.account.id):
                top_account_by_accountId[solution.account.id] = {
                    'account': solution.account,
                    'score': 0,
                }
            top_account_by_accountId[solution.account.id]['score'] += solution.score

        s = sorted(top_account_by_accountId.items(), reverse=True, key=lambda x: x[1])
        return [item[1] for item in s]
