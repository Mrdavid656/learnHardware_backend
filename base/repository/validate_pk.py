from base.utils import CommonResponseUtil


def validatePk(pk, model):
    try:
        model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise CommonResponseUtil.response_not_found()
    except pk is None:
        raise CommonResponseUtil.response_not_found()
