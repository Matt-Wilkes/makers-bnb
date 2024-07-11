from datetime import timedelta

def consolidate_bookings(all_bookings):
    bookings = {
        'id': [],
        'requester_id': [],
        'spaces_id': [],
        'check-in': [],
        'check-out': [],
        'status': [],
        'owner_id': []
    }
    
    if not all_bookings:
        return bookings
    
    all_bookings.sort(key=lambda x: (x.spaces_id, x.date))
    
    current_booking = {
        'id': all_bookings[0].id,
        'requester_id': all_bookings[0].requester_id,
        'spaces_id': all_bookings[0].spaces_id,
        'check-in': all_bookings[0].date,
        'check-out': all_bookings[0].date,
        'status': all_bookings[0].status,
        'owner_id': all_bookings[0].owner_id
    }
    
    for i in range(1, len(all_bookings)):
        booking = all_bookings[i]
        last_date = current_booking['check-out']
        
        if (booking.date == last_date + timedelta(days=1) and
            booking.spaces_id == current_booking['spaces_id'] and
            booking.requester_id == current_booking['requester_id']):
            # Extend the current booking
            current_booking['check-out'] = booking.date
        else:
            # Save the current booking and start a new one
            for key in current_booking:
                bookings[key].append(current_booking[key])
            
            current_booking = {
                'id': booking.id,
                'requester_id': booking.requester_id,
                'spaces_id': booking.spaces_id,
                'check-in': booking.date,
                'check-out': booking.date,
                'status': booking.status,
                'owner_id': booking.owner_id
            }
    
    # Append the last processed booking
    for key in current_booking:
        bookings[key].append(current_booking[key])
    
    return bookings
