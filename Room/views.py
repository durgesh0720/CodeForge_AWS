from django.shortcuts import render, redirect
from django.contrib import messages
from codeEditor.models import File,CurrentOutput
from .models import Room

def create_room(request):
    if request.method == 'POST':
        context = {}
        room = None
        try:
            file_id = request.POST.get('file_id')
            file = File.objects.get(id=file_id)
            try:
                file_output = CurrentOutput.objects.get(file=file)
            except:
                file_output = None
            room_id = f"{request.user.username}{file_id}{file.file_name}"[:20]

            room, created = Room.objects.get_or_create(file=file, defaults={"file_id": file_id})

            context['room_id'] = room_id
            context['file'] = file
            context['file_output'] = file_output
            context['username'] = request.user.username

            print(f'Context: {context}')
            return render(request, 'Room_Editor_Page.html', context)
        except Exception as e:
            print("Exception from create room: ", e)
            messages.error(request, f"Error creating room: {str(e)}")
            return redirect('dashboard')

def join_room(request):
    if request.method == 'POST':
        context = {}
        room_id = request.POST.get('room_id')

        try:
            room = Room.objects.get(room_id=room_id)

            context['room_id'] = room_id
            context['file'] = room.file
            context['file_output'] = CurrentOutput.objects.get(file=room.file)
            context['username'] = request.user.username

            print(f'Context: {context}')
            return render(request, 'Room_Editor_Page.html', context)
        except Room.DoesNotExist:
            messages.error(request, "Room not found!")
        except Exception as e:
            messages.error(request, f"Error joining room: {str(e)}")

        return redirect('dashboard')
