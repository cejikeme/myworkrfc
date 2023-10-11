@load base/protocols/conn

event zeek_init()
{
    Log::disable_stream(Conn::LOG);
}

event connection_attempt(c: connection)
{
    print fmt("TCP event: connection_attempt - %s:%d -> %s:%d", c$id$orig_h, c$id$orig_p, c$id$resp_h, c$id$resp_p);
}

event connection_established(c: connection)
{
    print fmt("TCP event: connection_established - %s:%d -> %s:%d", c$id$orig_h, c$id$orig_p, c$id$resp_h, c$id$resp_p);
}

event connection_finished(c: connection)
{
    print fmt("TCP event: connection_finished - %s:%d -> %s:%d", c$id$orig_h, c$id$orig_p, c$id$resp_h, c$id$resp_p);
}

event connection_first_ACK(c: connection)
{
    print fmt("TCP event: connection_first_ACK - %s:%d -> %s:%d", c$id$orig_h, c$id$orig_p, c$id$resp_h, c$id$resp_p);
}

event connection_half_finished(c: connection)
{
    print fmt("TCP event: connection_half_finished - %s:%d -> %s:%d", c$id$orig_h, c$id$orig_p, c$id$resp_h, c$id$resp_p);
}

event connection_partial_close(c: connection)
{
    print fmt("TCP event: connection_partial_close - %s:%d -> %s:%d", c$id$orig_h, c$id$orig_p, c$id$resp_h, c$id$resp_p);
}

event connection_pending(c: connection)
{
    print fmt("TCP event: connection_pending - %s:%d -> %s:%d", c$id$orig_h, c$id$orig_p, c$id$resp_h, c$id$resp_p);
}

event connection_rejected(c: connection)
{
    print fmt("TCP event: connection_rejected - %s:%d -> %s:%d", c$id$orig_h, c$id$orig_p, c$id$resp_h, c$id$resp_p);
}

event connection_reset(c: connection)
{
    print fmt("TCP event: connection_reset - %s:%d -> %s:%d", c$id$orig_h, c$id$orig_p, c$id$resp_h, c$id$resp_p);
}

event connection_reused(c: connection)
{
    print fmt("TCP event: connection_reused - %s:%d -> %s:%d", c$id$orig_h, c$id$orig_p, c$id$resp_h, c$id$resp_p);
}

event connection_state_remove(c: connection)
{
    print fmt("TCP event: connection_state_remove - %s:%d -> %s:%d", c$id$orig_h, c$id$orig_p, c$id$resp_h, c$id$resp_p);
}

event connection_status_update(c: connection)
{
    print fmt("TCP event: connection_status_update - %s:%d -> %s:%d", c$id$orig_h, c$id$orig_p, c$id$resp_h, c$id$resp_p);
}

event connection_timeout(c: connection)
{
    print fmt("TCP event: connection_timeout - %s:%d -> %s:%d", c$id$orig_h, c$id$orig_p, c$id$resp_h, c$id$resp_p);
}

event new_connection(c: connection)
{
    print fmt("TCP event: new_connection - %s:%d -> %s:%d", c$id$orig_h, c$id$orig_p, c$id$resp_h, c$id$resp_p);
}

event partial_connection(c: connection)
{
    print fmt("TCP event: partial_connection - %s:%d -> %s:%d", c$id$orig_h, c$id$orig_p, c$id$resp_h, c$id$resp_p);
}   
