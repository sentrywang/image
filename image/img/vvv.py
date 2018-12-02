from django.shortcuts import get_object_or_404, render
from common.render import r
from common.views import StaffBaseView, BaseView
from notice.models import Notice


class ForNoticeView(BaseView):
    post_params = ['image', 'genre', 'content', 'title']

    def valid_data(self, content, title, genre):
        if content == '':
            return 'INVALID_NOTICE_CONTENT'
        elif title == '':
            return 'INVALID_NOTICE_TITLT'
        elif genre == '':
            return 'INVALID_NOTICE_GENRE'
        return


class ListNotice(ForNoticeView):
    """公告列表"""
    def get(self, request):
        notices = Notice.objects.all()
        result = [x.to_dict() for x in notices]
        return r('OK', result)


class CreateNotice(ForNoticeView):
    """新增公告"""
    def get(self, request):

        return render(request, 'up.html')

    def post(self, request):
        data = request.form
        content = data['content']
        title = data['title']
        genre = data['genre']
        mesg = self.valid_data(content, title, genre)
        if mesg:
            return r(mesg)
        notice = Notice(content=content, title=title, genre=genre, image=request.FILES.get('img'))
        notice.save()
        return r('OK')


class EditNotice(ForNoticeView):
    """编辑公告"""

    def post(self, request, notice_id):
        data = request.data
        content = data['content']
        title = data['title']
        genre = data['genre']
        mesg = self.valid_data(content, title, genre)
        if mesg:
            return r(mesg)
        notice = get_object_or_404(Notice, id=notice_id)
        notice.content = content
        notice.title = title
        notice.genre = genre
        notice.image = request.FILES.get('img')
        notice.save()

        return r('OK')


class DeleteNotice(ForNoticeView):
    """删除公告"""

    def get(self, request, notice_id):
        notice = get_object_or_404(Notice, id=notice_id)
        notice.mark_delete()
        return r('OK')


class PublishNotice(ForNoticeView):
    """发布公告"""

    def get(self, request, notice_id):
        notice = get_object_or_404(Notice, id=notice_id)
        notice.mark_publish()
        return r('OK')


class UnpublishNotice(ForNoticeView):
    """下架公告"""

    def get(self, request, notice_id):
        notice = get_object_or_404(Notice, id=notice_id)
        notice.mark_unpublish()
        return r('OK')
