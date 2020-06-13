import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

function NavBar() {
    return (
        <div>
            <AppBar position="sticky" color="secondary">
                <Toolbar>
                    <Typography variant="h6" color="purple">
                        Is it an Onion?
                    </Typography>
                    <a className="NavBar-link" href="https://www.facebook.com">Link 1</a>
                    <a className="NavBar-link" href="https://www.github.com">Link 2</a>
                    <a className="NavBar-link" href="https://www.reddit.com">Link 3</a>                    
                </Toolbar>
            </AppBar>
        </div>
    );
}

export default NavBar;